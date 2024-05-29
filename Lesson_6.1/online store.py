import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_shopping_checkout(browser):
    browser.get("https://www.saucedemo.com/")
    
    # Войти в систему как стандартный пользователь
    username = browser.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    
    password = browser.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    
    login_button = browser.find_element(By.ID, "login-button")
    login_button.click()
    
    # Добавить товары в корзину
    products = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    for product in products:
        add_button = browser.find_element(By.XPATH, f"//div[text()='{product}']/following-sibling::div/button")
        add_button.click()
    
    # Перейти в корзину и оформить заказ
    cart_button = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_button.click()
    
    checkout_button = browser.find_element(By.XPATH, "//a[text()='CHECKOUT']")
    checkout_button.click()
    
    # Заполнить форму оформления заказа
    first_name = browser.find_element(By.ID, "first-name")
    first_name.send_keys("John")
    
    last_name = browser.find_element(By.ID, "last-name")
    last_name.send_keys("Doe")
    
    postal_code = browser.find_element(By.ID, "postal-code")
    postal_code.send_keys("12345")
    
    continue_button = browser.find_element(By.XPATH, "//input[@type='submit']")
    continue_button.click()
    
    # Прочитанная общая сумма
    total_amount = browser.find_element(By.CLASS_NAME, "summary_total_label")
    
    assert total_amount.text == "$58.29"