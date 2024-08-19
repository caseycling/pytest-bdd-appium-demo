Feature: Shopping Cart

  Scenario: Add an item to the cart
    Given I am logged in
    When I add the "Sauce Labs Backpack" to the cart
    Then the cart should have "1" item

  Scenario: Remove an item from the cart
    Given I am logged in
    When I add the "Sauce Labs Backpack" to the cart
    And I go to the shopping cart
    And I remove the "Sauce Labs Backpack" from the cart
    Then the cart should be empty