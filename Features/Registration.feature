
Feature: Verifying login functionality

    @sanity
    Scenario: Login with valid data
    Given User is on registration page
    When User enters username
    And User enters password
    And User click on signup button
    Then User should be logged successfully

    @sanity @smoke
    Scenario: Login with invalid username data
    Given User is on registration page
    When User enters invalid username
    And User enters password
    And User click on signup button
    Then User should NOT be registered successfully

    @sanity
    Scenario: Login with invalid password data
    Given User is on registration page
    When User enters invalid username
    And User enters invalid password
    And User click on signup button
    Then User should NOT be registered successfully

