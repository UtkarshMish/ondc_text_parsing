from flask import Blueprint, render_template

home_route = Blueprint("home", __name__)


@home_route.route("/", defaults={"path": ""})
@home_route.route("/<path:path>")
def home_page(path: str = None):

    return render_template("index.html")
