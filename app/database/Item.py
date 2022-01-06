from datetime import datetime
from typing import List, Optional

from app.database.meta.Descriptor import Descriptor
from app.database.meta.Price import Price
from beanie import Document
from pydantic import Field


class Item(Document):
    id: str = Field(...)
    parent_item_id: Optional[str] = Field(None)
    descriptor: Descriptor = Field(...)
    category_id: Optional[str] = Field(None)
    price: Price = Field(...)
    location_id: Optional[str] = Field(None)
    time: datetime = Field(...)
    tags: List[str] = Field(...)
    matched: Optional[bool] = Field(None)
    related: Optional[bool] = Field(None)
    recommended: Optional[bool] = Field(None)

    @staticmethod
    async def getItems(page: int = 1):
        LIMIT = 50
        OFFSET = LIMIT * (page - 1) if page > 1 else 0
        return await Item.aggregate(
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
