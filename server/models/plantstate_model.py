from enum import unique
from app import db
    
class PlantState(db.Model):
    state = db.Column(db.Integer, unique=True)
    #filepath to associated plant image
    img = db.Column(db.String(128), index=True)
    flower = db.Column(db.Boolean)
    #TODO: unsure if following needed
    next_state = db.Column(db.Integer)
    prev_state = db.Column(db.Integer)

    def __repr__(self):
        return '<User {}>'.format(self.state)