from .db import db
from datetime import datetime


class Mood(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    mood = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, index=True, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Mood for {self.user.username}>'

    def get_dict(self):
        return {
            'mood': self.mood,
            'user': self.user.username,
            'date_created': self.date_created
        }
