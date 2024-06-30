import pytest
import requests
from Lesson_8_1.Constants import Clients_URL

@pytest.fixture()
def get_token(username='donatello', password='does-machines'):
    log_pass = {'username': username, 'password': password}
    resp_token = requests.post(Clients_URL + '/auth/login', json=log_pass)
    token = resp_token.json()['userToken']
    return token