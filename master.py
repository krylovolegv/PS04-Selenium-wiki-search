from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import random
import time

# Установка geckodriver
service = FirefoxService(executable_path=GeckoDriverManager().install())

# Создаём объект браузера, через который мы будем действовать.
browser = webdriver.Firefox(service=service)


def get_paragraphs():
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    return [p.text for p in paragraphs if p.text]


def get_related_links():
    links = []
    # Ищем ссылки в элементах div с классом "hatnote navigation-not-searchable"
    hatnotes = browser.find_elements(By.CSS_SELECTOR, "div.hatnote.navigation-not-searchable a")
    links.extend([hatnote.get_attribute("href") for hatnote in hatnotes])

    # Также ищем все ссылки внутри основного контента статьи
    content_links = browser.find_elements(By.CSS_SELECTOR, "#mw-content-text a[href^='/wiki/']")
    for link in content_links:
        href = link.get_attribute("href")
        if href.startswith("https://ru.wikipedia.org/wiki/"):
            links.append(href)

    return links


def main():
    # Открываем сайт Википедии
    browser.get(
        "https://ru.wikipedia.org/wiki")

    while True:
        action = input("Выберите действие: 1 - Листать параграфы, 2 - Перейти на связанную страницу, 3 - Выйти: ")

        if action == "1":
            paragraphs = get_paragraphs()
            for para in paragraphs:
                print(para)
                time.sleep(1)  # Даем немного времени для прочтения
        elif action == "2":
            links = get_related_links()
            if links:
                link = random.choice(links)
                browser.get(link)
                print(f"Переход по ссылке: {link}")
            else:
                print("Связанных страниц не найдено.")
        elif action == "3":
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

    # Закрываем браузер
    browser.quit()


if __name__ == "__main__":
    main()


