import pytest
from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.common.by import By

# Scenarios
scenarios('../features/content_desc.feature')

@given("I have opened the Android app")
def open_android_app(android_rdc_driver):
    pass  # The app is opened via the fixture

@when("I locate the element by resource-id")
def locate_element_by_resource_id(android_rdc_driver):
    android_rdc_driver.element = android_rdc_driver.find_element(By.ID, "com.saucelabs.mydemoapp.android:id/productIV")

@then("the element should be displayed")
def check_element_displayed(android_rdc_driver):
    assert android_rdc_driver.element.is_displayed()
