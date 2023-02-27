from math import log, sin
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

LINK = 'https://suninjuly.github.io/alert_accept.html'

INPUT_VALUE = (By.XPATH, '//span[@id="input_value"]')
TEXT_FIELD = (By.XPATH, '//input[@id="answer"]')
SUBMIT = (By.XPATH, '//button[@class="btn btn-primary"]')

def calc(x):
  return str(log(abs(12*sin(int(x)))))

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(LINK)

driver.find_element(*SUBMIT).click()
confirm = driver.switch_to.alert
confirm.accept()

x = int(driver.find_element(*INPUT_VALUE).text)
driver.find_element(*TEXT_FIELD).send_keys(calc(x))
driver.find_element(*SUBMIT).click()

alert = driver.switch_to.alert
result = alert.text.split(':')[1]
print(result)

driver.quit()
