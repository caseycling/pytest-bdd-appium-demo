import pytest
from os import environ

from selenium import webdriver
from appium import webdriver as appiumdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

import time

# @pytest.fixture(scope="function")
# def setup():
#     options = ChromeOptions()
#     options.browser_version = 'latest'
#     options.platform_name = 'Windows 11'
#     sauce_options = {}
#     sauce_options['username'] = environ['SAUCE_USERNAME']
#     sauce_options['accessKey'] = environ['SAUCE_ACCESS_KEY']
#     sauce_options['build'] = 'Mobile web tests'
#     sauce_options['name'] = 'Example test'
#     options.set_capability('sauce:options', sauce_options)

#     url = "https://ondemand.us-west-1.saucelabs.com:443/wd/hub"
#     driver = webdriver.Remote(command_executor=url, options=options)

#     # run commands and assertions
#     yield driver
#     # end the session
#     driver.execute_script("sauce:job-result=" + jobStatus)
#     driver.quit()

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
    
# @pytest.fixture(scope="function")
# def android_rdc_driver():
#     options = UiAutomator2Options()
#     options['platformName'] = 'Android'
#     options['appium:app'] = 'storage:filename=SauceLabs-Demo-App.apk' # The filename of the mobile app
#     options['appium:deviceName'] = 'Android GoogleAPI Emulator'
#     options['appium:platformVersion'] = 'current_major'
#     options['appium:automationName'] = 'UiAutomator2'
#     options['sauce:options'] = {}
#     options['sauce:options']['username'] = 'caseyclinga1'
#     options['sauce:options']['accessKey'] = '45be69a0-2e06-493d-8731-f0d605b4044d'
#     options['sauce:options']['build'] = '<your build id>'
#     options['sauce:options']['name'] = '<your test name>'
#     options['sauce:options']['deviceOrientation'] = 'PORTRAIT'

#     # start the session
#     url = 'https://ondemand.us-west-1.saucelabs.com:443/wd/hub'
#     driver = appiumdriver.Remote(url, options)

#     yield driver
#     # replace with commands and assertions
#     time.sleep(5)
#     jobStatus = 'passed' # or 'failed'

#     # end the session
#     driver.execute_script('sauce:job-result=' + jobStatus)
#     driver.quit()