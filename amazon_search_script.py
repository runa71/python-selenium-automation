from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
# driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(executable_path='/Users/nilufayesmin/Desktop/AutomationQA/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/')

driver.find_element(By.ID,'twotabsearchtextbox').send_keys('table')
driver.find_element(By.ID,'nav-search-submit-button').click()

expected_result = '"table"'
actual_result = driver.find_element(By.CSS_SELECTOR, 'span.a-color-state.a-text-bold').text
assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}'
print('Test Case Passed!')

driver.quit()


