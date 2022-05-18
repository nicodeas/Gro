from server import app,db
from flask import redirect, render_template, request, url_for
from .models import User
from flask_login import login_user, logout_user, current_user, login_required

@app.route('/index')
def index():
    return render_template('landing/base_site.html')

@app.route('/game')
def load_game():
    return render_template('game/game_page.html')

@app.route('/register',methods=["POST","GET"])
def register_user():
    if request.method=="POST":
        username= request.form['username']
        password = request.form['password']
        new_user = User(username= username, password_hash=password)
        db.session.add(new_user)
        db.session.commit()
        # redirect not working
        return redirect(url_for('index'))
    else:
        return render_template('user/signup.html')

@app.route('/login',methods=["GET","POST"])
def login_user():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return render_template('user/login.html')