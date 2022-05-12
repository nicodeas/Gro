from datetime import datetime
from app import db
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    #user preferred name
    pref_name = db.Column(db.String(64), index=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    #rating for user based on number of completed plants
    user_rating = db.Column(db.Integer, index=True)
    #TODO: decide if dob necessary
    #  dob = db.Column(db.Date)

    def __repr__(self):
        return '<User {}>'.format(self.username)
 