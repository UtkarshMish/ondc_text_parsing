from beanie import Document


class Country(Document):
    name: str
    code: str
