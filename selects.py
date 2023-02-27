from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

LINK = 'https://suninjuly.github.io/selects1.html'
NUM1 = (By.XPATH, '//span[@id="num1"]')
NUM2 = (By.XPATH, '//span[@id="num2"]')
SELECT = (By.XPATH, '//select[@id="dropdown"]')
SUBMIT = (By.XPATH, '//button[@class="btn btn-default"]')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(LINK)

num1 = int(driver.find_element(*NUM1).text)
num2 = int(driver.find_element(*NUM2).text)
select = Select(driver.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(num1 + num2))
driver.find_element(*SUBMIT).click()

alert = driver.switch_to.alert
result = alert.text.split(':')[1]
print(result)

driver.quit()
