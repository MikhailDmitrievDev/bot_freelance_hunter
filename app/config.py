import os

from dotenv import load_dotenv

load_dotenv()

TOKEN_BOT = os.getenv('bot_token')
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")


WEBLANCER_URL = os.getenv("WEBLANCER_URL")
AUTH_WEBLANCER = os.getenv("AUTH_WEBLANCER")
WL_FLAG_API_LOGIN = os.getenv("WL_FLAG_API_LOGIN")
WL_LOGIN_ACCUNT = os.getenv("WL_LOGIN_ACCUNT")
WL_PASSWORD_ACCOUNT = os.getenv("WL_PASSWORD_ACCOUNT")
WL_STORE_LOGIN = os.getenv("WL_STORE_LOGIN")
REQUEST_WL_PREFIX = os.getenv("REQUEST_WL_PREFIX")

MONGO_URL = os.getenv("MONGO_URL")