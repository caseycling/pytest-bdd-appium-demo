Feature: SauceDemo Testing

  Scenario: Verify the title of the SauceDemo site
    Given I open the SauceDemo site
    Then the title should be "Swag Labs"

  Scenario: Login with correct credentials
    Given I open the SauceDemo site
    When I enter the correct username "standard_user"
    And I enter the correct password "secret_sauce"
    And I click the login button
    Then I should be redirected to the inventory page

  Scenario: Login with incorrect credentials
    Given I open the SauceDemo site
    When I enter the incorrect username "wrong name"
    And I enter the incorrect password "password"
    And I click the login button
    Then I should see the error message "Epic sadface: Username and password do not match any user in this service"