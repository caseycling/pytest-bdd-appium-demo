Feature: Add Item To Shopping Cart

  Scenario: Add an item to the cart
    Given I am logged in
    When I add the "Sauce Labs Backpack" to the cart
    Then the cart should have "1" item