from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time

# Установка geckodriver
service = FirefoxService(executable_path=GeckoDriverManager().install())

# Создаём объект браузера, через который мы будем действовать.
browser = webdriver.Firefox(service=service)

# Открываем браузер
browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
time.sleep(5)

# Закрываем браузер
browser.quit()

