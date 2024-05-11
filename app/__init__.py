from flask import Flask
from .routes import bp as api_bp

def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_DICT'] = True
    app.register_blueprint(api_bp)

    return app
