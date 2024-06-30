# открыть страницу в Хром
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# Открыть окно
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(5)

# Кликнуть по кнопке
driver.find_element(By.CSS_SELECTOR, "div.modal-footer p").click()
sleep(5)
driver.quit()
