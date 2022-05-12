# Gro

## Setting up environment

Run:

```
cd ./server
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


