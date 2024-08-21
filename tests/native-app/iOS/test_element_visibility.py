from selenium.webdriver.common.by import By

def test_element(ios_driver):

    element = ios_driver.find_element(By.XPATH, '//XCUIElementTypeOther[@name="Sauce Labs Backpack"]')
    
    assert element.is_displayed(), "The Sauce Labs Backpack element is not displayed"