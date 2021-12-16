from flask import Flask


def create_app():
    app = Flask(__name__)
    from .main import main_bp

    app.register_blueprint(main_bp)
    from .api import api_bp

    app.register_blueprint(api_bp)
    return app
