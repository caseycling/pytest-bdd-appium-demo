from selenium import webdriver
from os import environ

from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

# Load the scenarios from the feature file
scenarios('shopping_cart.feature')

@given("I am logged in")
def login(mobile_web_driver):
    driver = mobile_web_driver
    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

@when('I add the "Sauce Labs Backpack" to the cart')
def add_item_to_cart(mobile_web_driver):
    driver = mobile_web_driver
    add_to_cart_btn = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_to_cart_btn.click()

@when("I go to the shopping cart")
def go_to_cart(mobile_web_driver):
    driver = mobile_web_driver
    shopping_cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    shopping_cart_link.click()

@when('I remove the "Sauce Labs Backpack" from the cart')
def remove_item_from_cart(mobile_web_driver):
    driver = mobile_web_driver
    remove_item_btn = driver.find_element(By.ID, 'remove-sauce-labs-backpack')
    remove_item_btn.click()

@then('the cart should have "1" item')
def check_cart_item(mobile_web_driver):
    driver = mobile_web_driver
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1"

@then("the cart should be empty")
def check_cart_empty(mobile_web_driver):
    driver = mobile_web_driver
    cart_badge = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(cart_badge) == 0




