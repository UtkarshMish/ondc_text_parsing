from typing import Dict, Literal

from pydantic import BaseModel, Field


class Scalar(BaseModel):
    class Range(BaseModel):
        min: float
        max: float

    type: Literal["CONSTANT", "VARIABLE"] = Field(
        ...,
    )
    value: float
    estimated_value: float
    computed_value: float
    range: Range
    unit: str
