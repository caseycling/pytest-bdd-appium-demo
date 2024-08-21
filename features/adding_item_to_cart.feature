Feature: Adding item to cart

Scenario: Add Sauce Labs Backpack to cart
    Given I am on the Sauce Labs Backpack product page
    When I add the product to the cart
    Then The cart should show 1 item