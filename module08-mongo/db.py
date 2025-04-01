from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from main import get_settings
from models.product import Product


async def init_db():
    my_config = get_settings()
    client = AsyncIOMotorClient(my_config.connection_string)
    await init_beanie(database=client.get_default_database(), document_models=[Product])
