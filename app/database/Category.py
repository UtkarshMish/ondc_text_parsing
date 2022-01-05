from datetime import datetime
from typing import List, Optional

from app.database.meta.Descriptor import Descriptor
from beanie import Document


class Category(Document):
    id: str
    parent_category_id: Optional[str]
    descriptor: Descriptor
    time: datetime
    tags: List[str]
