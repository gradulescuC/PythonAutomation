Feature: Login functionality
Scenario: Successful Login with Valid entries
Given user navigates to the website facebook.com
And user logs in through Login link by using username as "pritysharma321@yahoo.com" and password as "prity123sharma"

Then login must be successful.
Scenario:  Unsuccessful Login with Invalid entries
Given user navigates to the website facebook.com
When username is incorrect, but the password is correct - user logs in through Login link by using Username as "Parma321@yahoo.com" and Password as "prity123sharma"
When username is correct, but the password is incorrect - user logs in through Login link by using username as "pritysharma321@yahoo.com" and Password as "12345678"
Then login must be unsuccessful.