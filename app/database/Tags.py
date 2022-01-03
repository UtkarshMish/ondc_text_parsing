from pydantic import BaseModel


class Tags(BaseModel):
    id: str
    name: str
