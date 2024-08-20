from selenium import webdriver
from selenium.webdriver.common.by import By
from appium import webdriver
from appium.options.common import AppiumOptions

import pytest
import os

@pytest.fixture
def ios_driver(scope='function'):

    options = AppiumOptions()
    options.set_capability('platformName', 'iOS')
    options.set_capability('appium:app', 'storage:filename=iOS-Real-Device-MyRNDemoApp.ipa')
    options.set_capability('appium:deviceName', 'iPhone.*')
    options.set_capability('appium:automationName', 'XCUITest')
    
    sauce_options = {
        'appiumVersion': 'latest',
        'username': os.getenv('SAUCE_USERNAME'),
        'accessKey': os.getenv('SAUCE_ACCESS_KEY'),
        'build': 'iOS',
        'name': 'Testing iOS'
    }
    options.set_capability('sauce:options', sauce_options)

    url = 'https://ondemand.us-west-1.saucelabs.com:443/wd/hub'
    driver = webdriver.Remote(command_executor=url, options=options)
    
    yield driver

    driver.quit()

def test_element(ios_driver):

    element = ios_driver.find_element(By.XPATH, '//XCUIElementTypeOther[@name="Sauce Labs Backpack"]')
    
    assert element.is_displayed(), "The Sauce Labs Backpack element is not displayed"

