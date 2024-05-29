from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открываем браузер и переходим на страницу
driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Ждем загрузки всех картинок
wait = WebDriverWait(driver, 10)
images = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "img")))

# Получаем значение атрибута src у 3-й картинки
third_image_src = images[3].get_attribute("src")
print(third_image_src)

# Закрываем браузер
driver.quit()