from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#landscape')))
src = driver.find_element(By.CSS_SELECTOR, '#award')

print(src.get_attribute('src'))
