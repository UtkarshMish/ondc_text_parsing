__all__ = ("connect_db",)


from os import environ

from app.database.Category import Category
from app.database.Country import Country
from app.database.Item import Item
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient


async def connect_db():
    client = AsyncIOMotorClient(environ.get("MONGODB_URI"))

    # Init beanie with the Product document class and a database
    await init_beanie(
        database=client[environ.get("DB_NAME")],
        document_models=[Category, Country, Item],
    )
