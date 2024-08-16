from appium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver


import pytest

def test_content_desc(android_rdc_driver):
    # Locate the element by resource-id
    element = android_rdc_driver.find_element(By.ID, "com.saucelabs.mydemoapp.android:id/productIV")

    # Assert the content-desc attribute
    assert element.get_attribute("contentDescription") == "Sauce Labs Bike Light"
