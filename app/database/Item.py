from datetime import datetime
from typing import Optional

from app.database.meta.Descriptor import Descriptor
from app.database.meta.Price import Price
from app.database.Tags import Tags
from pydantic import BaseModel, Field


class Item(BaseModel):
    id: str = Field(...)
    parent_item_id: str = Field(...)
    descriptor: Descriptor = Field(...)
    category_id: str = Field(...)
    price: Price = Field(...)
    location_id: str = Field(...)
    time: datetime = Field(...)
    tags: Tags = Field(...)
    matched: Optional[bool] = Field(None)
    related: Optional[bool] = Field(None)
    recommended: Optional[bool] = Field(None)
