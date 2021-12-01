Given the user on the user registration page.
When user enter invalid data on the page
| Fields|| Values|
| First Name            | User Name           |
| Last Name             | User Last Name      |
| Email Address         | someone@gmail.com    |
| Re-enter Email Address | someone@gmail.com   |
| Password              |PASSWORD|
| Birth-date              | 02|
Then the user registration should be successful.