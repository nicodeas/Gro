from server import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('landing/base_site.html')

@app.route('/game')
def load_game():
    return render_template('game/game_page.html')
