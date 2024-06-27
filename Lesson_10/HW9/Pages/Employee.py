import requests
import json
import allure
from Lesson_10.conftest import url

path = '/employee/'

class Employer:
    def __init__(self, url=url):
        self.url = url

    @allure.step()
    def get_list(self, company_id: int):
            company = {'company': company_id}
            response = requests.get(
                self.url + '/employee', params=company)
            return response.json()
    
    @allure.step()
    def add_new(self, token: str, body: json):
         headers = {'x-client-token': token}
         response = requests.post(
              self.url + '/employee', headers=headers, json=body)
            
        