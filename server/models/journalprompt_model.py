from datetime import datetime
from enum import unique
from app import db
    
class JournalPrompt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prompt = db.Column(db.String(255), nullable=False, unique=True)
    #is prompt a reflection question
    reflection = db.Column(db.Boolean, index=True, default=False)
    #below for potential implementation idea
    #mood_upper = db.Column(db.Integer, index=True)
    #mood_lower = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<User {}>'.format(self.prompt)