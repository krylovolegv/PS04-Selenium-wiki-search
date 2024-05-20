from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Установка geckodriver
service = FirefoxService(executable_path=GeckoDriverManager().install())

# Создаём объект браузера, через который мы будем действовать.
browser = webdriver.Firefox(service=service)

# Открываем сайт Википедии
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

# Проверяем по заголовку, тот ли сайт открылся
assert "Википедия" in browser.title

# Находим окно поиска
search_box = browser.find_element(By.ID, "searchInput")

# Вводим текст "Солнечная система"
search_box.send_keys("Солнечная система")

# Отправляем текст
search_box.send_keys(Keys.RETURN)

# Время ожидания 20 секунд
wait = WebDriverWait(browser, 300)

try:
    # Ожидаем, пока элемент станет видимым
    a = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Солнечная система")))
    print("Элемент найден")
    # Добавляем клик на элемент
    a.click()
except TimeoutException:
    print("Элемент не найден в течение указанного времени ожидания")



