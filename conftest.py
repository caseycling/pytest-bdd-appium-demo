import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def login(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")

    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys("standard_user") 

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")  # Replace "your_password" with the actual password

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()