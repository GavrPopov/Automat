# открыть страницу в Хром
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
Add_Element = "//button[contains(text(),'Add Element')]"
button = driver.find_element(By.XPATH, Add_Element)
# Кликнуть на кнопку Add Element 5 раз
for n in range(5):
    button.click()
    sleep(1)
  
sleep(5)
driver.quit()

# Собрать со страницы список кнопок
delete_button = driver.find_elements(By.XPATH, '//button(text = "Delete")')

#Вывести на экран размер списка
print(f"размер списка, {len(delete_button)}")
driver.quit()


# открыть страницу в FireFox
from selenium import webdriver
from webdriver_maneger.firefox import GeckDriverManager

driver = webdriver.FireFox()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
Add_Element = "//button[contains(text(), 'Add Element')]"
button = driver.find_element(By.XPATH, Add_Element)

# Кликнуть на кнопку Add Element 5 раз
for n in range(5):
    button.click()
    sleep(1)

sleep(5)
driver.quit()
# Собрать со страницы список кнопок
delete_button = driver.find_elements(By.XPATH, '//button(text = "Delete")')

#Вывести на экран размер списка
print(f"размер списка, {len(delete_button)}")
driver.quit()
