import pytest
from selenium import webdriver
from pages import LoginPage, ProductsPage, CartPage, CheckoutPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_shopping_cart(driver):
    login_page = LoginPage(driver)
    login_page.open("https://www.saucedemo.com/")
    login_page.login_as_standard_user()

    products_page = ProductsPage(driver)
    products_page.add_products_to_cart(["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"])
    products_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_out_form("Gavr", "Popov", "12345")
    total_price = checkout_page.get_total_price()

    assert total_price == "$58.29"