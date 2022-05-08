from datetime import datetime
from app import db
    
class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    state = db.Column(db.Integer, db.ForeignKey('plantstate.state'))
    last_session = db.Column(db.Integer, db.ForeignKey('session.id'))

    def __repr__(self):
        return '<User {}>'.format(self.id)