from flask import Flask

from app.routes import home_route


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(home_route)
    return app
