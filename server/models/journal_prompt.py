from .db import db


class JournalPrompt(db.Model):

    __tablename__ = 'journalprompt'

    id = db.Column(db.Integer, primary_key=True)
    prompt = db.Column(db.String(255))
    journals = db.relationship('JournalEntry', backref='journalprompt')

    def __repr__(self):
        return f'<JournalPrompt {self.prompt}>'

    def get_dict(self):
        return{
            'prompt': self.prompt
        }
