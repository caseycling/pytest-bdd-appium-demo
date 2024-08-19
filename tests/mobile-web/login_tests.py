import pytest
from pytest_bdd import scenarios, given, when, then

from os import environ

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.common.by import By

# Constants
URL = "https://www.saucedemo.com/"

# Scenarios
scenarios('../features/login.feature')

@pytest.fixture
def setup():
    options = ChromeOptions()
    options.browser_version = 'latest'
    options.platform_name = 'Windows 11'
    sauce_options = {}
    sauce_options['username'] = environ['SAUCE_USERNAME']
    sauce_options['accessKey'] = environ['SAUCE_ACCESS_KEY']
    sauce_options['build'] = 'Mobile web tests'
    sauce_options['name'] = 'Example test'
    options.set_capability('sauce:options', sauce_options)

    url = "https://ondemand.us-west-1.saucelabs.com:443/wd/hub"
    driver = webdriver.Remote(command_executor=url, options=options)

    # run commands and assertions
    yield driver
    # end the session
    driver.quit()

@given("I open the SauceDemo site")
def open_site(setup):
    setup.get(URL)

@then('the title should be "Swag Labs"')
def check_title(setup):
    assert "Swag Labs" in setup.title

@when('I enter the correct username "standard_user"')
def enter_username(setup):
    username_input = setup.find_element(By.ID, "user-name")
    username_input.send_keys("standard_user")

@when('I enter the correct password "secret_sauce"')
def enter_password(setup):
    password_input = setup.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")
    
@when('I enter the incorrect username "wrong name"')
def enter_username(setup):
    username_input = setup.find_element(By.ID, "user-name")
    username_input.send_keys("wrong name")

@when('I enter the incorrect password "password"')
def enter_password(setup):
    password_input = setup.find_element(By.ID, "password")
    password_input.send_keys("password")

@when("I click the login button")
def click_login(setup):
    login_button = setup.find_element(By.ID, "login-button")
    login_button.click()

@then("I should be redirected to the inventory page")
def check_inventory_page(setup):
    assert setup.current_url == "https://www.saucedemo.com/inventory.html"

@then('I should see the error message "Epic sadface: Username and password do not match any user in this service"')
def check_error_message(setup):
    error_element = setup.find_element(By.CSS_SELECTOR, "[data-test='error']")
    assert error_element.text == "Epic sadface: Username and password do not match any user in this service"
    assert setup.current_url == URL