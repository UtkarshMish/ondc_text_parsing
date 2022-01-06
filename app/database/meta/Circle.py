from app.database.meta.Scalar import Scalar
from pydantic import BaseModel, Field


class Circle(BaseModel):
    gps: str = Field(
        ...,
        regex="^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$",
    )
    redius: Scalar = Field(...)
