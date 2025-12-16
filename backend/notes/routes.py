from flask import Blueprint, request, jsonify
from backend.notes.services import list_notes, get_note, create_note, update_note, delete_note

bp = Blueprint('notes', __name__)

@bp.get('')
def list_route():
    q = request.args.get('q')
    return jsonify(list_notes(q))

@bp.get('/<int:note_id>')
def get_route(note_id):
    return jsonify(get_note(note_id))

@bp.post('')
def create_route():
    data = request.get_json(force=True) or {}
    title = data.get('title') or ''
    content = data.get('content') or ''
    if not title:
        return jsonify({ 'error': { 'code': 'INVALID', 'message': 'title required' } }), 400
    return jsonify(create_note(title, content))

@bp.put('/<int:note_id>')
def update_route(note_id):
    data = request.get_json(force=True) or {}
    title = data.get('title') or ''
    content = data.get('content') or ''
    if not title:
        return jsonify({ 'error': { 'code': 'INVALID', 'message': 'title required' } }), 400
    return jsonify(update_note(note_id, title, content))

@bp.delete('/<int:note_id>')
def delete_route(note_id):
    delete_note(note_id)
    return jsonify({ 'ok': True })