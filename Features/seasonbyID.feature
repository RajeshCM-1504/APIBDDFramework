@regression
Feature: Getting specific season based on ID
  # This is to get data for the specific season API

  Scenario Outline: Verify get season by ID API functionality
    Given the season details to be fetched based on ID from deltatre sports platform with parameter {locale} variable
    When we execute the Get season by ID GETAPI method
    Then season details is displayed based on ID
    Examples:
      | locale |
      | en-us |