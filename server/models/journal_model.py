from datetime import datetime
from app import db
    
class Journal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', nullable=False))
    session_id = db.Column(db.Integer, db.ForeignKey('session.id'))
    #is journal entry a reflection question?
    reflection = db.Column(db.Boolean, index=True, default=False)
    prompt_id = db.Column(db.Integer, db.ForeignKey('journalprompt.id'), nullable=False)
    #TODO: test unicode data in journal entries
    entry = db.Column(db.String(255))

    def __repr__(self):
        return '<User {}>'.format(self.id)