import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

LINK = 'https://suninjuly.github.io/file_input.html'

FIRST_NAME = (By.XPATH, '//input[@name="firstname"]')
LAST_NAME = (By.XPATH, '//input[@name="lastname"]')
EMAIL = (By.XPATH, '//input[@name="email"]')
FILE = (By.XPATH, '//input[@id="file"]')
SUBMIT = (By.XPATH, '//button[@type="submit"]')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'data.txt')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(LINK)

driver.find_element(*FIRST_NAME).send_keys('Roman')
driver.find_element(*LAST_NAME).send_keys('Sandutsa')
driver.find_element(*EMAIL).send_keys('sandutsar@yahoo.com')
driver.find_element(*FILE).send_keys(file_path)
driver.find_element(*SUBMIT).click()

alert = driver.switch_to.alert
result = alert.text.split(':')[1]
print(result)

driver.quit()
