import requests
import allure
import pytest
import unittest
from Diplom.Config import Site_URL
from Diplom.Config import Site_URL_2
from Diplom.Config import TOKEN


@allure.feature("API")
@allure.story("Получение списка книг")
@pytest.mark.api_test
@pytest.mark.positive_test

def test_get_books():
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }
    response = requests.get(f"https://{Site_URL_2}/products", headers=headers)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"



@allure.feature("API")
@allure.story("Получение информации о книге по ID")
@pytest.mark.api_test
@pytest.mark.positive_test

def test_get_book_by_id():
    book_id = "master-i-margarita-3018590"   
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

    response = requests.get(f"https://{Site_URL}/products/slug/{book_id}", headers=headers)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"
    assert "Булгаков" in response.text
    
@allure.feature("API")
@allure.story("Поиск книг на кириллице")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_search_books_rus():
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

    response = requests.get(f"https://{Site_URL_2}/search/product?phrase=гарри поттер и филосовский камень", headers=headers)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"

@allure.feature("API")
@allure.story("Поиск книг на латинице")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_search_books_eng():
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

    response = requests.get(f"https://{Site_URL_2}/search/product?phrase=harry-potter and the philosophers stone", headers=headers)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"

@allure.feature("API")
@allure.story("Получение списка книг по категории")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_get_category_books():
        headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

        response = requests.get(f"https://{Site_URL_2}/products?forceFilters[categories]=110322", headers=headers)
        assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"

@allure.feature("API")
@allure.story("Получение списка книг по фильтрам")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_get_filtres_books():
        headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

        response = requests.get(f"https://{Site_URL_2}/products?filters[onlyNew]=1", headers=headers)
        assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"      


@allure.feature("API")
@allure.story("Получение списка книг по автору")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_get_books_by_author():      
        headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

        response = requests.get(f"https://{Site_URL_2}/products/facet?filters[authors]=567533", headers=headers)
        assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}" 

@allure.feature("API")
@allure.story("Получение списка книг по наличию")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_get_available_books():
        headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

        response = requests.get(f"https://{Site_URL_2}/products/facet?filters[onlyAvailable]=1", headers=headers)
        assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}" 

@allure.feature("API")
@allure.story("Добавление книги в корзину")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_add_book_to_cart():
    data = {
        "id": '2444651',
        "adData": {
            "item_list_name": "search",
            "product_shelf": ""
        }
    }
    
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

    response = requests.post(f"https://{Site_URL}/cart/product", json=data, headers=headers)
    assert response.status_code == 400, f"Ожидался статус-код 200, но получен {response.status_code}"

@allure.feature("API")
@allure.story("Получение списка товаров в корзине")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_get_cart():
    
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

    response = requests.get(f"https://{Site_URL}/cart", headers=headers)
    assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"

@allure.feature("API")
@allure.story("Удаление книги из корзины")
@pytest.mark.api_test
@pytest.mark.positive_test
def test_del_book_from_cart():
    
    headers = {
        'content-type': 'application/json',
        'authorization': f'Bearer {TOKEN}'
    }

    response = requests.delete(f"https://{Site_URL}/cart", headers=headers)
    assert response.status_code == 204, f"Ожидался статус-код 200, но получен {response.status_code}"
