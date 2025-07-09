# Created by rajeshcm at 08/07/25
@regression
Feature: Getting competations based on ID
  # This is to get data for the API getcompetationsID

  Scenario Outline: Verify get competations by ID API functionality
    Given the competations details to be fetched based on ID from deltatre sports platform with parameter {locale} variable
    When we execute the Get CompetationsID GETAPI method
    Then competations list is displayed based on ID
    Examples:
      | locale |
      | en-us  |