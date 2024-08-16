import pytest
from os import environ

from selenium import webdriver
from appium import webdriver as appiumdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

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

# @pytest.fixture
# def android_rdc_driver(request):

#     username_cap = environ['SAUCE_USERNAME']
#     access_key_cap = environ['SAUCE_ACCESS_KEY']
    
#     caps = {
#         'username': username_cap,
#         'accessKey': access_key_cap,
#         'deviceName': 'Google.*',
#         'platformName': 'Android',
#         'build': 'RDC-Android-Python-Best-Practice',
#         'name': 'name-test',
#         'app': "https://github.com/saucelabs/sample-app-mobile/releases/download/2.7.1/Android.SauceLabs.Mobile.Sample.app.2.7.1.apk"
#     }

#     sauce_url = 'http://ondemand.us-west-1.saucelabs.com/wd/hub'

#     driver = appiumdriver.Remote(sauce_url, options=caps)
#     yield driver
#     sauce_result = "failed" if request.node.rep_call.failed else "passed"
#     driver.execute_script("sauce:job-result={}".format(sauce_result))
#     driver.quit()

@pytest.fixture(scope="function")
def android_rdc_driver():

    options = ChromeOptions()
    options.browser_version = 'latest'
    options.platform_name = 'Windows 11'
    sauce_options = {}
    sauce_options['username'] = environ['SAUCE_USERNAME']
    sauce_options['accessKey'] = environ['SAUCE_ACCESS_KEY']
    sauce_options['build'] = '<your build id>'
    sauce_options['name'] = '<your test name>'
    options.set_capability('sauce:options', sauce_options)

    url = "https://ondemand.us-west-1.saucelabs.com:443/wd/hub"
    driver = webdriver.Remote(command_executor=url, options=options)

    yield driver
    # end the session
    driver.quit() 