from sqlalchemy import create_engine
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

from config import (POSTGRES_DB, POSTGRES_PASSWORD,
                    POSTGRES_HOST, POSTGRES_PORT, POSTGRES_USER, MONGO_URL)

engine = create_engine(
    f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}")
client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
MONGO_URL = "<connection string>"

try:
      client.admin.command('ping')
      print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)