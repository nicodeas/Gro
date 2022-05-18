from server import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('landing/base_site.html')

@app.route('/game')
def load_game():
    return render_template('game/game_page.html')

@app.route('/register')
def register_user():
    return render_template('user/signup.html')

@app.route('/login')
def login_user():
    return render_template('user/login.html')