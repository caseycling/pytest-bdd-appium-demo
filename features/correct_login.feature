Feature: Login functionality

Scenario: Login with correct credentials
  Given I open the SauceDemo site
  When I enter the correct username "standard_user"
  And I enter the correct password "secret_sauce"
  And I click the login button
  Then I should be redirected to the inventory page