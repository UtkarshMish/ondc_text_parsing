from datetime import datetime

from app.database.meta.Descriptor import Descriptor
from app.database.Tags import Tags
from pydantic import BaseModel


class Category(BaseModel):
    id: str
    parent_category_id: str
    descriptor: Descriptor
    time: datetime
    tags: Tags
