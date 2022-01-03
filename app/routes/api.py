from app.models import BecknResponse
from flask import Blueprint, make_response, request

api_route = Blueprint("apis", __name__, url_prefix="/api")


@api_route.get("/search")
def search_for_product():
    json_data = request.json

    response = make_response()  # Todo: convert ml response to becknresponse and return
    return response


__all__ = ("api_route",)
