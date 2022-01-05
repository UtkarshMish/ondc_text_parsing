from app.database import connect_db
from app.database.Item import Item
from app.models import BecknResponse
from flask import Blueprint, make_response, request

api_route = Blueprint("apis", __name__, url_prefix="/api")


@api_route.get("/search")
def search_for_product():
    json_data = request.json

    response = make_response()  # Todo: convert ml response to becknresponse and return
    return response


@api_route.get("/products")
async def get_products():
    await connect_db()
    page = int(request.args.get("page") or 1)
    LIMIT = 50
    OFFSET = LIMIT * (page - 1) if page > 1 else 0

    items = await Item.aggregate(
        [
            {"$skip": OFFSET},
            {"$limit": LIMIT},
            {
                "$lookup": {
                    "from": "Category",
                    "localField": "category_id",
                    "foreignField": "_id",
                    "as": "category",
                }
            },
            {"$unwind": {"path": "$category"}},
            {
                "$unset": [
                    "category_id",
                    "matched",
                    "location_id",
                    "recommended",
                    "related",
                    "parent_item_id",
                ]
            },
            {"$set": {"category": "$category.descriptor.name"}},
        ]
    ).to_list()
    return {"products": items}


__all__ = ("api_route",)
