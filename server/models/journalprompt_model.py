from datetime import datetime
from app import db
    
class JournalPrompt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prompt = db.Column(db.String(255))
    #below for potential implementation idea
    #mood_upper = db.Column(db.Integer, index=True)
    #mood_lower = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<User {}>'.format(self.prompt)