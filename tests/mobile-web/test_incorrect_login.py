from pytest_bdd import scenarios, given, when, then

from selenium.webdriver.common.by import By

# Constants
URL = "https://www.saucedemo.com/"

# Scenarios
scenarios('../features/login.feature')

@given("I open the SauceDemo site")
def open_site(mobile_web_driver):
    mobile_web_driver.get(URL)

@when('I enter the incorrect username "wrong name"')
def enter_username(mobile_web_driver):
    username_input = mobile_web_driver.find_element(By.ID, "user-name")
    username_input.send_keys("wrong name")

@when('I enter the incorrect password "password"')
def enter_password(mobile_web_driver):
    password_input = mobile_web_driver.find_element(By.ID, "password")
    password_input.send_keys("password")

@when("I click the login button")
def click_login(mobile_web_driver):
    login_button = mobile_web_driver.find_element(By.ID, "login-button")
    login_button.click()

@then('I should see the error message "Epic sadface: Username and password do not match any user in this service"')
def check_error_message(mobile_web_driver):
    error_element = mobile_web_driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert error_element.text == "Epic sadface: Username and password do not match any user in this service"
    assert mobile_web_driver.current_url == URL