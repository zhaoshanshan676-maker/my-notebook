from datetime import datetime
from backend.db import db

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), index=True, nullable=False)
    content = db.Column(db.Text, default='')
    summary = db.Column(db.Text, default='')
    keywords = db.Column(db.Text, default='')
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)