from datetime import datetime
from .db import db


class JournalEntry(db.Model):

    __tablename__ = 'journalentry'

    id = db.Column(db.Integer, primary_key=True)
    entry = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    journal_prompt_id = db.Column(
        db.Integer, db.ForeignKey('journalprompt.id'))

    def __repr__(self):
        return f'<Journal entry for {self.user.username}>'

    def get_dict(self):
        return{
            'entry': self.entry,
            'date_created': self.date_created,
            'user': self.user.username,
            'journal_prompt': self.journalprompt.prompt if self.journalprompt else ""
        }
