Feature: Validate content description in Android app

  Scenario: Validate element by resource-id and check content description
    Given I have opened the Android app
    When I locate the element by resource-id
    Then the element should be displayed