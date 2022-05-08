from datetime import datetime
from app import db
    
class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    session_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    #id of last session TODO: not sure if this is a good idea
    last_sid = db.Column(db.Integer, db.ForeignKey('session.id'))
    mood = db.Column(db.Integet, index=True)
    water = db.Column(db.Boolean)
    fertilizer = db.Column(db.Boolean)
    sun = db.Column(db.Boolean)
    pot_state = db.Column(db.Integer, index=True)
    plant_state = db.Column(db.Integer, db.ForeignKey('plantstate.state'))
    journal_id = db.Column(db.Integer, db.ForeignKey('journal.id'))


    def __repr__(self):
        return '<User {}>'.format(self.id)
 