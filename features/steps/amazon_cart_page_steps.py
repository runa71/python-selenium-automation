from behave import given, when, then
from selenium.webdriver.common.by import By


@when('Click Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.ID, 'nav-cart-count')