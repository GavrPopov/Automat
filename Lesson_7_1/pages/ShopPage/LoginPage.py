from selenium.webdriver.common.by import By
from constants import Shop_URL

class LoginPage:
    def __init__(self, browser, url=Shop_URL):
        self.browser = browser
        self.browser.implicitly_wait(4)
        self.browser.maximize_window()
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def sign_in(self, user_name, password):
        self.browser.find_element(By.CSS_SELECTOR, '#user-name').send_keys(user_name)
        self.browser.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
        self.browser.find_element(By.CSS_SELECTOR, '#login-button').click()