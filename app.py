# app.py - Main Flask Application
from flask import Flask
from config import Config
from routes.main import main_bp

def create_app():
    """Creates and configures the Flask application."""
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configuration from Config class

    # Register blueprints
    app.register_blueprint(main_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
