from selenium.webdriver.common.by import By

def test_clicking_element(ios_driver):
    element = ios_driver.find_element(By.XPATH, '//XCUIElementTypeOther[@name="Sauce Labs Backpack"]')
    element.click()    
    
    add_to_cart_btn = ios_driver.find_element(By.ACCESSIBILITY_ID, "Add To Cart button")

    assert add_to_cart_btn.is_displayed(), "The image with accessibility id 'assets/src/assets/images/sauce-backpack.jpg' is not displayed."