import pytest
from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-ssl-errors=yes')
chrome_options.add_argument('--ignore-certificate-errors')


@pytest.fixture(scope="module")
def chrome_browser():
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    browser.quit()