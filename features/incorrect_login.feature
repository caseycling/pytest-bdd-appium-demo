Feature: Login functionality

Scenario: Login with incorrect credentials
    Given I open the SauceDemo site
    When I enter the incorrect username "wrong name"
    And I enter the incorrect password "password"
    And I click the login button
    Then I should see the error message "Epic sadface: Username and password do not match any user in this service"