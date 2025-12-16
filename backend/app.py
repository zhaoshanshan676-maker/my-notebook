from flask import Flask
from flask_cors import CORS
from backend.config import Config
from backend.db import init_db
from backend.notes.routes import bp as notes_bp
from backend.ai.routes import bp as ai_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    init_db(app)
    app.register_blueprint(notes_bp, url_prefix='/api/notes')
    app.register_blueprint(ai_bp, url_prefix='/api/ai')
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)