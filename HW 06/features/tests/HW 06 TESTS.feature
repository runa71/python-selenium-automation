Feature: Test on Sign In page


  Scenario: Verify that logged out user sees Sign In when clicking on Returns and Orders.
    Given Open Amazon page
    When Click Returns & Orders
    Then Verify user is brought to Sign In page