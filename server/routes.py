from server import app,db
from flask import flash, redirect, request, url_for,session
from .models import User, JournalPrompt,JournalEntry,Mood
from .controllers import GameController
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
    
@app.route('/login',methods=["POST"])
def user_login_post():
    
    ###input name fields
    username = request.form.get('username')
    password = request.form.get('password')
    ###
    
    
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password_hash,password):
        flash('Please check login details')
        return redirect(url_for('user_login'))
    login_user(user)
    GameController.update_user()
    return redirect(url_for('index'))


@app.route('/signup', methods=["POST"])
def signup_user_post():
    
    ###input name fields
    username = request.form.get('username')
    password = request.form.get('password')
    first_name = request.form.get('first-name')
    last_name= request.form.get('last-name')
    ###
    
    
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


@app.route('/create-journal-prompt', methods=["POST"])
@login_required
def create_journal_prompt():
    if current_user.username != 'admin':
        return redirect(url_for('index'))
    else:
        
        ###input name fields
        prompt = request.form.get('journal-prompt')
        ###
        
        
        if not prompt:
            return redirect(url_for('admin'))
        new_journal_prompt = JournalPrompt(prompt = prompt)
        db.session.add(new_journal_prompt)
        db.session.commit()
        return redirect(url_for('admin'))
    

@app.route('/journal',methods=["POST"])
@login_required
def post_journal():
    user_id = current_user.id
    
    ###input name fields
    prompt_id= session.get("prompt_id")
    entry = request.form.get('journal-entry')
    ###
    
    
    # do not post empty entries to db
    if not entry:
        return redirect(url_for('journal'))
    journal_entry = JournalEntry(user_id= user_id,entry=entry,journal_prompt_id=prompt_id)
    db.session.add(journal_entry)
    db.session.commit()
    GameController.update_journal_recorded()
    return redirect(url_for('journal'))

@app.route('/mood',methods=['POST'])
@login_required
def post_mood():
    
    ###input name fields
    mood = request.form.get("mood-entry")
    ###
    
    if mood=="":
        return redirect(url_for('mood'))
    new_mood = Mood(mood=mood,user_id=current_user.id)
    db.session.add(new_mood)
    db.session.commit()
    GameController.update_mood_recorded()
    return redirect(url_for('mood'))

@app.route('/breathing',methods=["POST"])
@login_required
def post_breathing():
    GameController.update_breathing_complete()
    return redirect(url_for('breathing'))

@app.route('/meditation',methods=["POST"])
@login_required
def post_meditation():
    GameController.update_meditation_complete()
    return redirect(url_for('activity'))