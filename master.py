from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import random

# Установка geckodriver
service = FirefoxService(executable_path=GeckoDriverManager().install())

# Создаём объект браузера, через который мы будем действовать.
browser = webdriver.Firefox(service=service)

# Открываем сайт Википедии
browser.get(
    "https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")

# Ищем все элементы div с классом "hatnote navigation-not-searchable"
hatnotes = []
for element in browser.find_elements(By.TAG_NAME, "div"):
    # Чтобы искать атрибут класса
    cl = element.get_attribute("class")
    if cl == "hatnote navigation-not-searchable":
        hatnotes.append(element)

if hatnotes:
    # Выбираем случайный элемент из найденных
    hatnote = random.choice(hatnotes)

    # Для получения ссылки находим тег "a" внутри тега "div"
    link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")

    # Переходим по ссылке
    browser.get(link)


