from datetime import datetime
from .db import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True,
                         unique=True, nullable=False)

    moods = db.relationship('Mood', backref="user")
    journals = db.relationship("JournalEntry", backref="user")

    plant_state = db.Column(db.Integer, default=-1)
    pot_state = db.Column(db.Integer, default=-1)

    user_rating = db.Column(db.Integer, default=0)

    mood_recorded = db.Column(db.Boolean, default=False)
    journal_recorded = db.Column(db.Boolean, default=False)
    activity_one_complete = db.Column(db.Boolean, default=False)
    activity_two_complete = db.Column(db.Boolean, default=False)

    date_created = db.Column(db.DateTime, default=datetime.utcnow())
    last_session = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def get_dict(self):
        return {
            'username': self.username,
            'date_created': self.date_created,
            'last_session': self.last_session,
            'user_rating': self.user_rating,
            'moods': [m.mood for m in self.moods],
            'journals': [j.entry for j in self.journals],
            'plant_state': self.plant_state,
            'pot_state': self.pot_state,
            'mood_recorded': self.mood_recorded,
            'journal_recorded': self.journal_recorded,
            'activity_one_complete': self.activity_one_complete,
            'activity_two_complete': self.activity_two_complete
        }
