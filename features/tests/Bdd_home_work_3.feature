# Created by nilufayesmin at 8/18/23
Feature: Sign Page Test Cases
  # Enter feature description here

  Scenario: Sign in page can be open from sign in pop up
    Given Open Amazon page
    When Click Sign In from popup
    Then  verify Clicking is working for sign in page

    # Enter steps here
  Scenario: Logged out user sees Sign in when clicking on returns and Orders
    Given Open Amazon page
    When Click Cart icon
    Then verify Clicking is working for sign in page