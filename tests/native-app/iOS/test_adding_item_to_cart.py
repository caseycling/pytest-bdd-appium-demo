from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.common.by import By

# Constants
scenarios('../features/adding_item_to_cart.feature')

@given('I am on the Sauce Labs Backpack product page')
def navigate_to_product_page(ios_driver):
    element = ios_driver.find_element(By.XPATH, '//XCUIElementTypeOther[@name="Sauce Labs Backpack"]')
    element.click()

@when('I add the product to the cart')
def add_item_to_cart(ios_driver):
    add_to_cart_btn = ios_driver.find_element(By.ACCESSIBILITY_ID, "Add To Cart button")
    add_to_cart_btn.click()

@then('The cart should show 1 item')
def check_cart_item_count(ios_driver):
    cart = ios_driver.find_element(By.ACCESSIBILITY_ID, "tab bar option cart")
    total_items_in_cart = cart.get_attribute("label")
    assert total_items_in_cart == "1"