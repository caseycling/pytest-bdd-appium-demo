from pytest_bdd import scenarios, given, then
from selenium.webdriver.common.by import By

# Constants
scenarios('../features/element.feature')

@given('I am on the Sauce Labs Backpack product page')
def navigate_to_product_page(ios_driver):
    element = ios_driver.find_element(By.XPATH, '//XCUIElementTypeOther[@name="Sauce Labs Backpack"]')
    element.click()

@then('The Sauce Labs Backpack element should be displayed')
def check_element_displayed(ios_driver):
    element = ios_driver.find_element(By.XPATH, '//XCUIElementTypeOther[@name="Sauce Labs Backpack"]')
    assert element.is_displayed(), "The Sauce Labs Backpack element is not displayed"
