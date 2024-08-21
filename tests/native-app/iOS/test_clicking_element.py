from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.common.by import By

# Constants
scenarios('../features/clicking_element.feature')

@given('I am on the Sauce Labs Backpack product page')
def navigate_to_product_page(ios_driver):
    element = ios_driver.find_element(By.XPATH, '//XCUIElementTypeOther[@name="Sauce Labs Backpack"]')
    element.click()

@when('I view the Add To Cart button')
def check_add_to_cart_button(ios_driver):
    add_to_cart_btn = ios_driver.find_element(By.ACCESSIBILITY_ID, "Add To Cart button")
    assert add_to_cart_btn.is_displayed(), "The image with accessibility id 'assets/src/assets/images/sauce-backpack.jpg' is not displayed."
