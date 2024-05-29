class CalculatorPage:
    def __init__(self, driver):
        self._driver = driver

    def open(self, url):
        self._driver.get(url)