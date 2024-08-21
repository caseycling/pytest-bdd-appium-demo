import pytest
from os import environ

from selenium import webdriver
from appium import webdriver as appiumdriver
from appium.options.android import UiAutomator2Options
from appium.options.common import AppiumOptions

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions


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

@pytest.fixture
def mobile_web_driver():
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

@pytest.fixture(scope="function")
def android_rdc_driver():

    options = UiAutomator2Options()
    options.browser_version = 'latest'
    sauce_options = {}
    sauce_options['username'] = environ['SAUCE_USERNAME']
    sauce_options['accessKey'] = environ['SAUCE_ACCESS_KEY']
    sauce_options['build'] = 'Native mobile android'
    sauce_options['name'] = 'pytest-bdd test'
    options.set_capability('appium:app', 'storage:filename=SauceLabs-Demo-App.apk')
    options.set_capability('sauce:options', sauce_options)
    options.set_capability('deviceName', 'Google_Pixel_5_sltech_us1')  
    options.set_capability('platformName', 'Android')  


    url = "https://ondemand.us-west-1.saucelabs.com:443/wd/hub"
    driver = appiumdriver.Remote(url, options=options)

    yield driver
    # end the session
    driver.quit() 

@pytest.fixture
def ios_driver(scope='function'):

    options = AppiumOptions()
    options.set_capability('platformName', 'iOS')
    options.set_capability('appium:app', 'storage:filename=iOS-Real-Device-MyRNDemoApp.ipa')
    options.set_capability('appium:deviceName', 'iPhone.*')
    options.set_capability('appium:automationName', 'XCUITest')
    
    sauce_options = {
        'appiumVersion': 'latest',
        'username': environ['SAUCE_USERNAME'],
        'accessKey': environ['SAUCE_ACCESS_KEY'],
        'build': 'iOS',
        'name': 'Testing iOS'
    }
    options.set_capability('sauce:options', sauce_options)

    url = 'https://ondemand.us-west-1.saucelabs.com:443/wd/hub'
    driver = appiumdriver.Remote(command_executor=url, options=options)
    
    yield driver

    driver.quit()
