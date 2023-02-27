from math import log, sin
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

LINK = 'https://suninjuly.github.io/explicit_wait2.html'

PRICE = (By.XPATH, '//h5[@id="price"]')
BOOK = (By.XPATH, '//button[@id="book"]')
INPUT_VALUE = (By.XPATH, '//span[@id="input_value"]')
TEXT_FIELD = (By.XPATH, '//input[@id="answer"]')
SUBMIT = (By.XPATH, '//button[@type="submit"]')

def calc(x):
  return str(log(abs(12*sin(int(x)))))

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(LINK)

WebDriverWait(driver, 15).until(
    EC.text_to_be_present_in_element(PRICE, '$100'))
driver.find_element(*BOOK).click()
x = int(driver.find_element(*INPUT_VALUE).text)
driver.find_element(*TEXT_FIELD).send_keys(calc(x))
driver.find_element(*SUBMIT).click()

alert = driver.switch_to.alert
result = alert.text.split(':')[1]
print(result)

driver.quit()
