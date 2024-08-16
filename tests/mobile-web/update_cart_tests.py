import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_add_item_to_cart(setup, login):
    driver = setup
    login
    
    add_to_cart_btn = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_to_cart_btn.click()

    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

    assert cart_badge.text == "1"

def test_remove_item_from_cart(setup, login):
    driver = setup
    login

    add_to_cart_btn = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_to_cart_btn.click()

    shopping_cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    shopping_cart_link.click()

    remove_item_btn = driver.find_element(By.ID, 'remove-sauce-labs-backpack')
    remove_item_btn.click()

    cart_badge = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")

    assert len(cart_badge) == 0





