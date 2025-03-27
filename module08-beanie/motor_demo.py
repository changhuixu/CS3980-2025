from motor.motor_asyncio import AsyncIOMotorClient
import asyncio


async def main():
    client = AsyncIOMotorClient("mongodb://localhost:27017/my_database")

    databases = await client.list_database_names()
    print(databases)

    default_database = client.get_default_database()
    print(default_database)

    server_info = await client.server_info()
    print(server_info)


asyncio.run(main())
