from flask import Flask

from app.routes import api_route, home_route


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(home_route)
    app.register_blueprint(api_route)
    return app
