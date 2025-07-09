# Created by rajeshcm at 08/07/25
@regression
Feature: Getting seasons based on ID
  # This is to get data for the API getcompetationsID

  Scenario Outline: Verify get seasons by ID API functionality
    Given the seasons details to be fetched based on ID from deltatre sports platform with parameter {locale} variable
    When we execute the Get seasons by ID GETAPI method
    Then seasons list is displayed based on ID
    Examples:
      | locale |
      | en-us  |