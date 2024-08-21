from pytest_bdd import scenarios, given, when, then

from selenium.webdriver.common.by import By

# Constants
URL = "https://www.saucedemo.com/"

# Scenarios
scenarios('../features/correct_login.feature')

@given("I open the SauceDemo site")
def open_site(mobile_web_driver):
    mobile_web_driver.get(URL)

@when('I enter the correct username "standard_user"')
def enter_username(mobile_web_driver):
    username_input = mobile_web_driver.find_element(By.ID, "user-name")
    username_input.send_keys("standard_user")

@when('I enter the correct password "secret_sauce"')
def enter_password(mobile_web_driver):
    password_input = mobile_web_driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")

@when("I click the login button")
def click_login(mobile_web_driver):
    login_button = mobile_web_driver.find_element(By.ID, "login-button")
    login_button.click()

@then("I should be redirected to the inventory page")
def check_inventory_page(mobile_web_driver):
    assert mobile_web_driver.current_url == "https://www.saucedemo.com/inventory.html"