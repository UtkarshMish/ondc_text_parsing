from numbers import Number
from typing import Dict, Literal

from pydantic import BaseModel, Field


class Scalar(BaseModel):
    class Range(BaseModel):
        min: Number
        max: Number

    type: Literal["CONSTANT", "VARIABLE"] = Field(
        ...,
    )
    value: Number
    estimated_value: Number
    computed_value: Number
    range: Range
    unit: str
