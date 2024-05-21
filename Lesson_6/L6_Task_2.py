from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get('http://uitestingplayground.com/textinput')
driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()
button = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text

sleep(2)
print(button)