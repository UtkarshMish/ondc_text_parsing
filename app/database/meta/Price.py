from decimal import Decimal

from pydantic import BaseModel


class Price(BaseModel):
    currency: str
    value: Decimal
    estimated_value: Decimal
    computed_value: Decimal
    listed_value: Decimal
    offered_value: Decimal
    minimum_value: Decimal
    maximum_value: Decimal
