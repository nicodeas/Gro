from datetime import datetime
from email.policy import default
from app import db
    
class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    session_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    #id of last session TODO: not sure if this is a good idea
    last_sid = db.Column(db.Integer, db.ForeignKey('session.id'))
    mood = db.Column(db.Integer, index=True)
    water = db.Column(db.Boolean, default=False)
    fertilizer = db.Column(db.Boolean, default=False)
    sun = db.Column(db.Boolean, default=False)
    pot_state = db.Column(db.Integer, index=True, nullable=False)
    plant_state = db.Column(db.Integer, db.ForeignKey('plantstate.state'), nullable=False)
    journal_id = db.Column(db.Integer, db.ForeignKey('journal.id'))


    def __repr__(self):
        return '<User {}>'.format(self.id)
 