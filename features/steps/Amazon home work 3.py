from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open Amazon page')
def Open_Amazon_page(context):
    context.driver.get('https://www.amazon.com/')


@when('Click Cart icon')
def click_on_cart_icon(context):
    context.driver.find_element(By.ID,'nav-cart-count').click()


@then('verify Clicking is working for sign in page')
def verify_clicking_is_working_for_sign_in_page(context):
    expected_result = 'Click Cart icon'
    actual_result = context.driver.find_element(By.CSS_SELECTOR,'.nav-line-1 nav-progressive-content').text
    assert expected_result == actual_result,f'Error, expected{ expected_result} did not match actual{ actual_result}'





