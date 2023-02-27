from math import log, sin
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

LINK = 'https://suninjuly.github.io/get_attribute.html'

IMAGE = (By.XPATH, '//img[@id="treasure"]')
TEXT_FIELD = (By.XPATH, '//input[@id="answer"]')
CHECKBOX = (By.XPATH, '//input[@id="robotCheckbox"]')
RADIOBUTTON = (By.XPATH, '//input[@id="robotsRule"]')
SUBMIT = (By.XPATH, '//button[@class="btn btn-default"]')

def calc(x):
  return str(log(abs(12*sin(int(x)))))

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(LINK)

x = int(driver.find_element(*IMAGE).get_attribute('valuex'))
driver.find_element(*TEXT_FIELD).send_keys(calc(x))
driver.find_element(*CHECKBOX).click()
driver.find_element(*RADIOBUTTON).click()
driver.find_element(*SUBMIT).click()

alert = driver.switch_to.alert
result = alert.text.split(':')[1]
print(result)

driver.quit()
