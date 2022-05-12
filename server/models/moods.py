from .db import db
from datetime import datetime


class Mood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mood = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
