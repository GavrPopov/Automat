# открыть страницу в Хром
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
import requests
from bs4 import BeautifulSoup

url = "http://uitestingplayground.com/ajax"
response = requests.get(url)

# Проверяем статус код ответа
if response.status_code == 200:
    # Нажимаем на кнопку и получаем текст из зеленой плашки
    data = {
        "ajaxButton": "true"
    }
    response = requests.post(url, data=data)
    
    # Парсим HTML страницу для извлечения текста из зеленой плашки
    soup = BeautifulSoup(response.text, 'html.parser')
    green_box_text = soup.find('div', class_='bg-success').get_text()

    # Выводим текст в консоль
    print(green_box_text)
else:
    print("Failed to fetch the page")
