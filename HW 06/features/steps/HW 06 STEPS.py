from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@given('Open Amazon page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()

@when('Click Returns & Orders')
def click_returns_and_orders(context):
    # context.driver.find_element(By.ID, 'nav-orders').click()
    context.app.main_page.click_returns_and_orders()

@then('Verify user is brought to Sign In page')
def verify_sign_in_page(context):
    # verify Sign in header is visible
    # context.driver.find_element(By.CSS_SELECTOR, 'h1[class="a-spacing-small"]')
    # # verify email input field is present
    # context.driver.find_element(By.ID, 'ap_email')
    context.app.sign_in_page.verify_sign_in_page()