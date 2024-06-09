import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_form_validation(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    # Заполнить форму
    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Иван")
    
    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Петров")
    
    address = browser.find_element(By.NAME, "address")
    address.send_keys("Ленина, 55-3")
    
    email = browser.find_element(By.NAME, "email")
    email.send_keys("test@skypro.com")
    
    phone = browser.find_element(By.NAME, "phone")
    phone.send_keys("+7985899998787")
    
    city = browser.find_element(By.NAME, "city")
    city.send_keys("Москва")
    
    country = browser.find_element(By.NAME, "country")
    country.send_keys("Россия")
    
    job_position = browser.find_element(By.NAME, "job")
    job_position.send_keys("QA")
    
    company = browser.find_element(By.NAME, "company")
    company.send_keys("SkyPro")
    
    # Отправить форму
    submit_button = browser.find_element(By.ID, "submit")
    submit_button.click()
    
    # Проверить цвета подтверждения
    zip_code = browser.find_element(By.NAME, "zip")
    assert "rgb(255, 0, 0)" in zip_code.value_of_css_property("border-color")
    
    other_fields = browser.find_elements(By.CSS_SELECTOR, ".form-control.is-valid")
    for field in other_fields:
        assert "rgb(40, 167, 69)" in field.value_of_css_property("border-color")