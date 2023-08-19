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
#
driver.find_element(By.CSS_SELECTOR,'.nav-input.nav-progressive-attribute')
driver.find_element(By.CSS_SELECTOR,'.nav-input.')