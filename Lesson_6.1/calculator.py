import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_slow_calculator(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    delay_input = browser.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.send_keys("45")
    
    buttons = browser.find_elements(By.CSS_SELECTOR, ".digit, .operator")
    
    for button in buttons:
        button.click()
        time.sleep(1)  
        
    # Дождаться завершения анимации
    result_window = browser.find_element(By.CSS_SELECTOR, "#result")
    
    time.sleep(45)

    # Дождаться появления результата после задержки
    assert result_window.text == "15"