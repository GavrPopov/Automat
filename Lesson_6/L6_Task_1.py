from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 20)
driver.get('http://uitestingplayground.com/ajax')
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))).text

sleep(2)
print(text)
