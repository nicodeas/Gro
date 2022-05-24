from server import app
from flask import redirect, render_template, url_for,session
from .models import JournalPrompt
from flask_login import current_user
import random

@app.route('/')
@app.route('/index')
def index():
    return render_template('landing/base_site.html')

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial/tutorial.html')

@app.route('/game')
def load_game():
    if not current_user.is_authenticated:
        return redirect(url_for('user_login'))
    return render_template('game/game_page.html')

@app.route('/login')
def user_login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return render_template('user/login.html')

@app.route('/signup')
def signup_user():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return render_template('user/signup.html')

@app.route('/admin')
def admin():
    if not current_user.is_authenticated or current_user.username != 'admin':
        return redirect(url_for('index'))
    return render_template('admin/admin.html')


@app.route('/meditation')
def meditation():
    if not current_user.is_authenticated:
        return redirect(url_for('user_login'))
    return render_template('game/meditation.html')

@app.route('/breathing')
def breathing():
    if not current_user.is_authenticated:
        return redirect(url_for('user_login'))
    return render_template('game/breathing.html')

@app.route('/journal')
def journal():
    if not current_user.is_authenticated:
        return redirect(url_for('user_login'))
    prompts = JournalPrompt.query.all()
    prompt = random.choice(prompts)
    session['prompt_id']=prompt.id
    return render_template('game/journal.html',prompt=prompt.prompt)