import pytest
from selenium import webdriver
from pages.Form_Page import FormPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_fill_form(driver):
    form_page = FormPage(driver)
    form_page.open("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    form_page.fill_form("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "", "Москва", "Россия", "QA", "SkyPro")
    form_page.submit_form()
    
    assert form_page.is_zip_code_highlighted_red()
    assert form_page.are_other_fields_highlighted_green()