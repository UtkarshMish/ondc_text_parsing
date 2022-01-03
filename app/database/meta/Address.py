from pydantic import BaseModel


class Address(BaseModel):
    door: str
    name: str
    building: str
    street: str
    locality: str
    ward: str
    city: str
    state: str
    country: str
    area_code: str
