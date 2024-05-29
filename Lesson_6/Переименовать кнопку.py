# открыть страницу в Хром
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Открываем браузер и переходим на страницу
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

# Находим поле ввода, вводим текст и нажимаем на кнопку
input_field = driver.find.element.by.id("textinput")
input_field.send_keys("SkyPro")
button = driver.find.element.by.id("textinput_button")
button.click()

# Ждем немного, чтобы страница обновилась
time.sleep(2)

# Получаем текст кнопки и выводим в консоль
button_text = button.text
print(button_text)

# Закрываем браузер
driver.quit()