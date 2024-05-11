from flask import Flask

def create_app():
    app = Flask(__name__)

    from . import routes
    # Register routes
    app.register_blueprint(routes.bp)

    return app
