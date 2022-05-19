from server import db, login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    
    first_name = db.Column(db.String(64),default='guest_user_first_name')
    last_name = db.Column(db.String(64),default='guest_user_last_name')
    
    username = db.Column(db.String(64), index=True,
                         unique=True, nullable=False)
    
    password_hash = db.Column(db.String(256),nullable=False)
    
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
    
    
    
class JournalPrompt(db.Model):

    __tablename__ = 'journalprompt'

    id = db.Column(db.Integer, primary_key=True)
    prompt = db.Column(db.String(255))
    journals = db.relationship('JournalEntry', backref='journalprompt')

    def __repr__(self):
        return f'<JournalPrompt {self.prompt}>'

    def get_dict(self):
        return{
            'prompt': self.prompt
        }


class JournalEntry(db.Model):

    __tablename__ = 'journalentry'

    id = db.Column(db.Integer, primary_key=True)
    entry = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, index=True, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    journal_prompt_id = db.Column(
        db.Integer, db.ForeignKey('journalprompt.id'))

    def __repr__(self):
        return f'<Journal entry for {self.user.username}>'

    def get_dict(self):
        return{
            'entry': self.entry,
            'date_created': self.date_created,
            'user': self.user.username,
            'journal_prompt': self.journalprompt.prompt if self.journalprompt else ""
        }

class Mood(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    mood = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, index=True, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Mood for {self.user.username}>'

    def get_dict(self):
        return {
            'mood': self.mood,
            'user': self.user.username,
            'date_created': self.date_created
        }