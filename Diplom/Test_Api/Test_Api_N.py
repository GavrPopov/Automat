import requests
import allure
import pytest
import unittest
from Diplom.Config import Site_URL_2
from Diplom.Config import TOKEN

@allure.feature("API")
@allure.story("Символы юникода")
@pytest.mark.api_test
@pytest.mark.negative_test
def test_search_unicode_symbols():
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

    response = requests.get(f"https://{Site_URL_2}/search/product?phrase=✉ § © ☯ ☭ ? $ £ *", headers=headers)
    assert response.status_code == 422, f"Ожидался статус-код 422, но получен {response.status_code}"

@allure.feature("API")
@allure.story("Пробел")
@pytest.mark.api_test
@pytest.mark.negative_test
def test_search_space():
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

    response = requests.get(f"https://{Site_URL_2}/search/product?phrase=   ", headers=headers)
    assert response.status_code == 422, f"Ожидался статус-код 422, но получен {response.status_code}"