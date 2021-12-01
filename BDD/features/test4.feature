Feature: Registration
Background:

Given user on the homepage
And user follows "Sign in"

@regression
Scenario: Create a New User
When user fills "registration email textbox" with "chitrali.sharma27@gmail.com"
And user clicks "create an account button"
And user enters the following details
| First Name | Chitrali|
| Last Name | Sharma|
| Password | Inquiry@1234 |
  And user clicks "register button"

Scenario: User does not follow form validations
When user enters wrong characters
Then error message displayed with invalid password
And user returns back on registration page


