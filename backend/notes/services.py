from backend.notes.models import Note
from backend.db import db
from datetime import datetime

def list_notes(q=None):
    query = Note.query
    if q:
        like = f"%{q}%"
        query = query.filter((Note.title.ilike(like)) | (Note.content.ilike(like)))
    notes = query.order_by(Note.updated_at.desc()).all()
    return [{ 'id': n.id, 'title': n.title, 'updated_at': n.updated_at.isoformat() } for n in notes]

def get_note(note_id):
    n = Note.query.get_or_404(note_id)
    return { 'id': n.id, 'title': n.title, 'content': n.content, 'summary': n.summary, 'keywords': n.keywords.split(',') if n.keywords else [], 'updated_at': n.updated_at.isoformat() }

def create_note(title, content):
    n = Note(title=title, content=content, updated_at=datetime.utcnow())
    db.session.add(n)
    db.session.commit()
    return get_note(n.id)

def update_note(note_id, title, content):
    n = Note.query.get_or_404(note_id)
    n.title = title
    n.content = content
    n.updated_at = datetime.utcnow()
    db.session.commit()
    return get_note(n.id)

def delete_note(note_id):
    n = Note.query.get_or_404(note_id)
    db.session.delete(n)
    db.session.commit()