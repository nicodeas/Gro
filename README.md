# Gro 🌱
Welcome to Gro, your friendly habit building and self-care guide. 😌

It can take 3 weeks to start building a habit. 📅

Almost anything is possible with a little help! Meet your very own plant friend, who will be there for you at every step. 💆🏻‍♂️

Check in with Gro every day, and be guided through interactive self-care exercises. 🌞

Look after your plant to look after yourself! 🧘🏻‍♂️

Gro is here for you. Start your self care journey today! ✨

---
## Purpose


---
## Architecture
This front-end of the website is built using HTML, JS and CSS, with the use of libraries including Bootstrap, Ajax and Jquery. The back-end of the website uses the python flask library.

Though unconventional practice in the software world today, the team decided to use a server side rendering architecture to simplify the authentication process and setting up a webserver to serve static frontend files. It also simplifies page routing and rendering and allows us to start the entire app with a single command.


---


## Setting up environment
Run:
```
pip install -r requirements.txt
```

---

## Add environment variables
Create a copy of .env-template and rename to .env

---

## DB setup
Create DB file (set to gro.db), run:

```
flask db migrate
```
Apply migrations, run:
```
flask db upgrade
```

---

## Start server
Run:
``` 
flask run
```
---

## Admin
1. Click on signup and create a user with username ```admin```
1. Once you are logged in as admin, click on the admin tab and add jounal prompts.
    - Please enter several prompts upon first launch of game

Only the admin user has access to the admin portal. Game will not be ready for users if this step is not complete.

---

## Testing
To test the application, run:
```
-
```


## Notes
The game page images are off-center due to the game art itself and not css alignment