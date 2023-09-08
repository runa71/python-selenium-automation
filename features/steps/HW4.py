from behave import given, when, then
from selenium.webdriver.common.by import By

HEADER_LINKS = (By.ID,'zg_header')


@given('Open Amazon BestSeller')
def open_amazon_bestseller(context):
    context.driver.get('https://www.amazon.com/Best-Sellers/zgbs/ref=zg_bs_tab_bsa')



@then('Verify that BestSeller has 5 links')
def click_on_bestseller(context):
    links = context.driver.find_elements(*HEADER_LINKS ).click()
    print(f'total links:{len(links)}')
    assert len(links) == 5, f'Expected 5 links but got{len(links)}'
