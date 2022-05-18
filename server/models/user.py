from datetime import datetime
from .db import db
from .moods import Mood
from werkzeug import generate_password_hash, check_password_hash
from flask_login import UserMixin
from server import login


class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True,
                         unique=True, nullable=False)

    moods = db.relationship('Mood', backref="user")
    journals = db.relationship("JournalEntry", backref="user")

    plant_state = db.Column(db.Integer, default=-1)
    pot_state = db.Column(db.Integer, default=-1)

    user_rating = db.Column(db.Integer, default=0)

    mood_recorded = db.Column(db.Boolean, default=False)
    journal_recorded = db.Column(db.Boolean, default=False)
    breathing_complete = db.Column(db.Boolean, default=False)
    meditation_complete = db.Column(db.Boolean, default=False)

    date_created = db.Column(db.DateTime, default=datetime.now())
    last_session = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f'<User {self.username}>'

    def get_dict(self):
        return {
            'username': self.username,
            'date_created': self.date_created,
            'last_session': self.last_session,
            'user_rating': self.user_rating,
            'moods': [m.mood for m in self.moods],
            'journals': [j.entry for j in self.journals],
            'plant_state': self.plant_state,
            'pot_state': self.pot_state,
            'mood_recorded': self.mood_recorded,
            'journal_recorded': self.journal_recorded,
            'breathing_complete': self.breathing_complete,
            'meditation_complete': self.meditation_complete
        }    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)        
    
    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))