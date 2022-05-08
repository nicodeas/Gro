from datetime import datetime
from app import db
    
class Journal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #TODO: is user_id necessary?
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    session_id = db.Column(db.Integer, db.ForeignKey('session.id'))
    #is journal a reflection question?
    reflection = db.Column(db.Boolean, index=True)
    prompt_id = db.Column(db.Integer, db.ForeignKey('journalprompt.id')
    #TODO: decide on appropriate answer length
    entry = db.Column(db.String(255))

    def __repr__(self):
        return '<User {}>'.format(self.id)