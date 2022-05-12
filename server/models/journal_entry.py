from datetime import datetime
from .db import db


class JournalEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entry = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
