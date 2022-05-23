# Testing manual

## Follow the instructions in the README to start the app

1. After connecting, ensure the following:

- That the navigation bar only contains the Home, About Us, Login and Sign Up buttons

2. Follow the login url to the login page

- Ensure that just the Username and Password fields are present and the navigation bar is not

3. Login with the admin account

- Ensure that the Account, Journal, Game, Activity, Admin and Logout buttons are now present

- Perform the daily tasks for the game and check the activity and journal pages for the updated content

4 Logout of the admin account

- Ensure that the navigation bar is back to how it was, with only the Home, About Us, Login and Sign Up buttons

5. Now having returned to the index page, click on the Sign Up button

- Ensure that there are four fields to enter data into (First name, Last name, Username, Password)

6. Create a new account with the following credentials:

    - First name: test-fname
    - Last name: test-lname
    - Username: test-uname
    - Password: test-pass


- After that, check that you are on the index page, with the Account, Journal, Game, Activity and Logout 
buttons visible on the navigation bar

7. Play the game again

- Check that the Journal and Activity pages correctly load and present the information from the latest 
game session

8. Logout from the test user

9. Run the python file within this directory

- python3 -m tests.test_cleanup
