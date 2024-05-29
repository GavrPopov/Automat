class FormPage:
    def __init__(self, driver):
        self._driver = driver

    def open(self, url):
        self._driver.get(url)

    def fill_form(self, first_name, last_name, address, email, phone, zip_code, city, country, job, company):
        # Implementation of form filling
        pass

    def submit_form(self):
        # Implementation of form submission
        pass

    def is_zip_code_highlighted_red(self):
        # Check if zip code is highlighted red
        pass

    def are_other_fields_highlighted_green(self):
        # Check if other fields are highlighted green
        pass
      