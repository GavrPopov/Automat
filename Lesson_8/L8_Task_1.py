import requests
import pytest
import time

BASE_URL = "https://x-clients-be.onrender.com" 

# Авторизация для получения токена доступа
def get_access_token():
    login_url = f"{BASE_URL}/auth/login"
    login_data = {
        "username": "donatello",
        "password": "does-machines"
    }
    response = requests.post(login_url, json=login_data)
    return response.json().get("access_token")

@pytest.fixture
def access_token():
    return get_access_token()

def test_get_employee(access_token):
    response = requests.get(f"{BASE_URL}/employee", headers={"Authorization": f"Bearer {access_token}"})
    time.sleep(120)
    assert response.status_code == 200

def test_post_employee(access_token):
    payload = {
        "name": "John Doe",
        "position": "Developer"
    }
    response = requests.post(f"{BASE_URL}/employee", json=payload, headers={"Authorization": f"Bearer {access_token}"})
    assert response.status_code == 201

def test_get_employee_by_id(access_token):
    response = requests.get(f"{BASE_URL}/employee/1", headers={"Authorization": f"Bearer {access_token}"})
    assert response.status_code == 200

def test_patch_employee_by_id(access_token):
    payload = {
        "position": "Senior Developer"
    }
    response = requests.patch(f"{BASE_URL}/employee/1", json=payload, headers={"Authorization": f"Bearer {access_token}"})
    assert response.status_code == 200

# Проверка обязательности полей
def test_required_fields(access_token):
    required_fields = ["name", "position"]
    response = requests.get(f"{BASE_URL}/employee", headers={"Authorization": f"Bearer {access_token}"})
    schema = response.json()
    for field in required_fields:
        assert field in schema["properties"]