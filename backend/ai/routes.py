from flask import Blueprint, request, jsonify
from backend.notes.models import Note
from backend.db import db
from backend.ai.services import summarize_text, enhance_text

bp = Blueprint('ai', __name__)

@bp.post('/summarize')
def summarize_route():
    data = request.get_json(force=True) or {}
    note_id = data.get('note_id')
    if not note_id:
        return jsonify({ 'error': { 'code': 'INVALID', 'message': 'note_id required' } }), 400
    n = Note.query.get_or_404(note_id)
    try:
        out = summarize_text(n.content or n.title)
    except Exception as e:
        return jsonify({ 'error': { 'code': 'AI_ERROR', 'message': str(e) } }), 400
    n.summary = out
    db.session.commit()
    return jsonify({ 'summary': out, 'keywords': [] })

@bp.post('/enhance')
def enhance_route():
    data = request.get_json(force=True) or {}
    text = data.get('text') or ''
    if not text:
        return jsonify({ 'error': { 'code': 'INVALID', 'message': 'text required' } }), 400
    try:
        out = enhance_text(text)
    except Exception as e:
        return jsonify({ 'error': { 'code': 'AI_ERROR', 'message': str(e) } }), 400
    return jsonify({ 'enhanced_text': out })