from selenium.webdriver.common.by import By


def test_adding_item_to_cart(ios_driver):
    element = ios_driver.find_element(By.XPATH, '//XCUIElementTypeOther[@name="Sauce Labs Backpack"]')
    element.click()    
    
    add_to_cart_btn = ios_driver.find_element(By.ACCESSIBILITY_ID, "Add To Cart button")
    add_to_cart_btn.click()    

    cart = ios_driver.find_element(By.ACCESSIBILITY_ID, "tab bar option cart")
    total_items_in_cart = cart .get_attribute("label")

    assert total_items_in_cart == "1"