from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click Sign In from popup')
def click_sigin_popup(context):
    context.driver.find_element(By.CSS_SELECTOR, '.a-spacing-small').click()


@then('verify Clicking is working for sign in page')
def verify_clicking_is_working(context):
    expected_result='Click Sign In from popup'
    actual_result = context.driver.find_element(By.CSS_SELECTOR,'.a-spacing-small')
    assert expected_result == actual_result,f'Error,expected{ expected_result}did not match  actual{actual_result}'