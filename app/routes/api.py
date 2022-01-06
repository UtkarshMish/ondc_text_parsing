from datetime import datetime
from typing import Dict, Literal

from app.database import connect_db
from app.database.Item import Item
from app.models import BecknResponse
from flask import Blueprint, make_response, request

api_route = Blueprint("apis", __name__, url_prefix="/api")


@api_route.post("/search")
async def search_for_product():
    await connect_db()
    json_data: Dict[Literal["search", "page"], str] = request.json
    search_query = json_data.get("search")
    page_query = int(json_data["page"]) if json_data.get("page") else 1
    product_list = (
        await Item.getItems(page_query) if not search_query else list()
    )  # Todo: convert ml response to becknresponse and return

    total = await Item.count() if not search_query else 1
    response = make_response(
        BecknResponse(
            context=BecknResponse.ContextType(
                domain="domain",
                action="search",
                bap_id="123",
                bpp_uri="123",
                city="telangana",
                core_version="1.0",
                country="IN",
                message_id="123",
                timestamp=datetime.now().isoformat(),
                transaction_id="123",
            ),
            message=BecknResponse.MessageType(
                intent=[{}], fulfillment=[{"product": product_list}, {"total": total}]
            ),
        ).dict()
    )
    return response


@api_route.get("/products")
async def get_products():
    await connect_db()
    page = int(request.args.get("page") or 1)

    items = await Item.getItems(page)
    return {"products": items, "total": await Item.count()}


__all__ = ("api_route",)
