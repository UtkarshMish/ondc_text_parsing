from pydantic import BaseModel, Field


class Descriptor(BaseModel):
    name: str
    code: str
    symbol: str
    short_desc: str
    long_desc: str
    images: str
    audio: str
    threeD_render: str = Field(alias="3d_render")
