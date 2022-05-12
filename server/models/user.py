from datetime import datetime
from .db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True,
                         unique=True, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    last_session = db.Column(db.DateTime)
    # rating for user based on number of completed plants
    user_rating = db.Column(db.Integer, index=True)

    moods = db.relationship('Mood', backref="user")
    journals = db.relationship("JournalEntry", backref="user")

    plant_state = db.Column(db.Integer, default=-1)
    pot_state = db.Column(db.Integer, default=-1)

    mood_recorded = db.Column(db.Boolean, default=False)
    journal_recorded = db.Column(db.Boolean, default=False)
    activity_one_complete = db.Column(db.Boolean, default=False)
    activity_two_complete = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)
