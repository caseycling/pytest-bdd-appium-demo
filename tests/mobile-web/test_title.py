from pytest_bdd import scenarios, given, when, then

from selenium.webdriver.common.by import By

# Constants
URL = "https://www.saucedemo.com/"

# Scenarios
scenarios('../features/login.feature')

@given("I open the SauceDemo site")
def open_site(mobile_web_driver):
    mobile_web_driver.get(URL)

@then('the title should be "Swag Labs"')
def check_title(mobile_web_driver):
    assert "Swag Labs" in mobile_web_driver.title