# Created by rajeshcm at 08/07/25
@smoke
Feature: Getting stadiums based on multiple parameters
  # This is to get data for the API stadiums information

  Scenario Outline: Verify stadiums using multiple parameters API functionality
    Given the stadium details to be fetched from deltatre sports platform with the team ID is {teamId} And the stadium ID is {stadiumId} And the season IDs are {seasonIds} And the locale is {locale}
    When we execute the Get stadiums GETAPI method
    Then stadium information is displayed
    Examples:
      | teamId                                                | stadiumId                                               | seasonIds                                               | locale |
      | cpl ::Football_Team::a92c57ab1d2041c4bfb1856a00645ace | cpl::Football_Stadium::0b84d157b99d4a22abe15dc4c3a59216 | cpl::Football_Season::ef4074023d99497e9c973a1dc98007fb, | en-us  |