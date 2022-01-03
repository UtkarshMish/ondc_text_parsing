from datetime import datetime

from app.database.City import City
from app.database.Country import Country
from app.database.meta import Circle, Descriptor
from app.database.meta.Address import Address
from pydantic import BaseModel, Field


class Location(BaseModel):
    id: str
    descriptor: Descriptor
    gps: str = Field(
        ...,
        regex="^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$",
    )
    address: Address
    station_code: str
    city: City
    country: Country
    circle: Circle
    polygon: str
    threeDspace: str = Field(..., alias="3dspace")
    time: datetime
