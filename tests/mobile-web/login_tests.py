import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://www.saucedemo.com/"

def test_saucedemo_title(setup):
    driver = setup
    driver.get(URL)
    assert "Swag Labs" in driver.title
    # Add more test steps as needed

def test_saucedemo_login(setup):
    driver = setup
    driver.get(URL)

    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys("standard_user") 

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce") 

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

def test_incorrect_credentials(setup):
    driver = setup
    driver.get(URL)

    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys("wrong name") 

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("password")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    
    assert error_message.text == "Epic sadface: Username and password do not match any user in this service"
    assert driver.current_url == URL




