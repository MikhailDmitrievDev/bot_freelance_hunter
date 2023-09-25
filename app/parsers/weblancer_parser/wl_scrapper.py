import json

from bs4 import BeautifulSoup

from .utils import post_request, get_request
from .schemas import WL_BASE_AUTH_MODEL, ResponseTemplate
from utils import CookiesManager
from config import (
    WEBLANCER_URL,
    AUTH_WEBLANCER,
    WL_FLAG_API_LOGIN,
    WL_LOGIN_ACCUNT,
    WL_PASSWORD_ACCOUNT,
    WL_STORE_LOGIN,
    REQUEST_WL_PREFIX
)


class AuthWeblance:
    body = {
        "action": WL_FLAG_API_LOGIN,
        "code": "",
        "login": WL_LOGIN_ACCUNT,
        "password": WL_PASSWORD_ACCOUNT,
        "store_login": WL_STORE_LOGIN,
    }
    url = WEBLANCER_URL + AUTH_WEBLANCER

    @classmethod
    async def get_hash_link_key(cls):
        response = await get_request("https://weblancer.net", cookies=CookiesManager.get_cookies(), headers={})
        soup = BeautifulSoup(response.get("body"), "html.parser")
        json_data = json.loads(soup.find('script', id='__NEXT_DATA__'))
        return json_data['buildId']

    @classmethod
    async def make_auth(cls):
        response = await post_request(cls.url, headers={}, body=cls.body)
        CookiesManager(response.get("cookies")).write_cookie()
        profile = await cls.get_profile()
        return profile

    @classmethod
    async def get_profile(cls):

        HASH_KEY = await cls.get_hash_link_key()
        prof_url = f"{WEBLANCER_URL}{REQUEST_WL_PREFIX}{HASH_KEY}/users/guest_1694859481282.json?login=guest_1694859481282"
        response = await get_request(prof_url, headers={}, cookies=CookiesManager.get_cookies())
        if response.get("status_code") == 200:
            profile = ResponseTemplate(**json.loads(response.get("body")))
            return profile
        return "Пользователь не авторизован"
