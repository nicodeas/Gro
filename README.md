# Gro

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


