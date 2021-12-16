from logging import debug
from flask import Flask


def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    from .main import main_bp

    app.register_blueprint(main_bp)
    from .api import api_bp

    app.register_blueprint(api_bp)
    return app
