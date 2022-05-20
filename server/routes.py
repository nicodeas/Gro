from datetime import datetime
from server import app,db
from flask import flash, redirect, render_template, request, url_for,session
from .models import User, JournalPrompt,JournalEntry
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
import random

@app.route('/')
@app.route('/index')
def index():
    return render_template('landing/base_site.html')

@app.route('/game')
@login_required
def load_game():
    return render_template('game/game_page.html')

@app.route('/login')
def user_login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return render_template('user/login.html')
    

@app.route('/login',methods=["POST"])
def user_login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password_hash,password):
        flash('Please check login details')
        return redirect(url_for('user_login'))
    login_user(user)
    return redirect(url_for('index'))


@app.route('/signup')
def signup_user():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return render_template('user/signup.html')

@app.route('/signup', methods=["POST"])
def signup_user_post():
    username = request.form.get('username')
    password = request.form.get('password')
    first_name = request.form.get('first-name')
    last_name= request.form.get('last-name')
    user = User.query.filter_by(username=username).first()
    if user:
        flash('User already exists.')
        return redirect(url_for('signup_user'))
    
    from .utils import validate_password
    
    if not validate_password(password):
        flash('Please enter a stronger password')
        return redirect(url_for('signup_user'))
    
    new_user=User(first_name=first_name,last_name=last_name,username=username, password_hash=generate_password_hash(password,method='sha256'))
    db.session.add(new_user)
    db.session.commit()
    login_user(new_user)
    return redirect(url_for('index'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/admin')
def admin():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    return render_template('admin/admin.html')

@app.route('/create-journal-prompt', methods=["POST"])
@login_required
def create_journal_prompt():
    if current_user.username != 'admin':
        return redirect(url_for('index'))
    else:
        prompt = request.form.get('journal-prompt')
        if not prompt:
            return redirect(url_for('admin'))
        new_journal_prompt = JournalPrompt(prompt = prompt)
        db.session.add(new_journal_prompt)
        db.session.commit()
        return redirect(url_for('admin'))
    
@app.route('/journal')
def journal():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    prompt = random.choice(JournalPrompt.query.all())
    session['prompt_id']=prompt.id
    return render_template('game/journal.html',prompt=prompt.prompt)

@app.route('/journal',methods=["POST"])
@login_required
def post_journal():
    user_id = current_user.id
    prompt_id= session.get("prompt_id")
    entry = request.form.get('journal-entry')
    # do not post empty entries to db
    if not entry:
        return redirect(url_for('journal'))
    journal_entry = JournalEntry(user_id= user_id,entry=entry,journal_prompt_id=prompt_id)
    current_user.journal_recorded=True
    current_user.last_session = datetime.now()
    db.session.add(journal_entry)
    db.session.commit()
    return redirect(url_for('journal'))