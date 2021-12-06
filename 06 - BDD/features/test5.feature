Feature: Login
Background:
Given user on the login page
And user follows "Log in"

@regression @smoke
Scenario: Verification of Login Function
Given user on the Login Page
And user enters "email address" with "chitrali.sharma27@gmail.com"
And user enters "password" with "Inquiry@1234"
And user click "log in" button
Then user should see "My Account"
Scenario: Unsuccessful login
Given user on the Login Page
And user enters "email address" with "chitrali.sharma27@gmail.com"
And user enters "password" with "qsder@1234"
And user clicks "login" button
Then error message displayed with wrong password
And user returns back on login page