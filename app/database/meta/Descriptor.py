from typing import List, Optional

from pydantic import BaseModel, Field


class Descriptor(BaseModel):
    name: str
    code: Optional[str]
    symbol: Optional[str]
    short_desc: Optional[str]
    long_desc: Optional[str]
    images: Optional[List[str]]
    audio: Optional[str]
    threeD_render: Optional[str] = Field(alias="3d_render")
