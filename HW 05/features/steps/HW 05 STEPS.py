from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then



ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
PRODUCT_NAME = (By.ID, 'productTitle')
COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")
@given('Open product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/gp/product/{product_id}/')

@when('Verify user can click through colors')
def verify_can_click_colors(context):
    expected_colors = ['Black', 'Blue Over Dye', 'Bright White', 'Dark Blue Vintage'] # 0, 1, 2, 3, 4
    colors = context.driver.find_elements(*COLOR_OPTIONS)
    actual_colors = []
    for color in colors[:4]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        actual_colors += [current_color]
    assert actual_colors == expected_colors, f'Expected {expected_colors} did not match actual {actual_colors}'

@when('Store product name')
def get_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.product_name}')

@then('Click on Add to cart')
def click_add_to_cart(context):
    sleep(3)
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(2)
