# открыть страницу в Хром
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr/")
Add_Element = 'button.btn-primary'
click=driver.find_element(By.CSS_SELECTOR, Add_Element)

# Три раза кликнуть по синей кнопке
for n in range(3):
    click.click()
    driver.swich_to.alert.accept()
    sleep(1)

sleep(5)
driver.quit()

# Открыть страницу в FireFox
from selenium import webdriver
from webdriver_maneger.firefox import GeckDriverManager
driver = webdriver.FireFox()
driver.get("http://uitestingplayground.com/dynamicid/")
driver.find_element(By.CSS_SELECTOR, 'button.btn')

# Три раза кликнуть по синей кнопке
for n in range(3):
    click.click()
    driver.swich_to.alert.accept()
    sleep(1)

sleep(5)
driver.quit()
