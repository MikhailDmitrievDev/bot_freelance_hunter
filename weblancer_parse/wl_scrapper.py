import json

from bs4 import BeautifulSoup

from weblancer_parse.utils import post_request, get_request
from weblancer_parse.schemas import WL_BASE_AUTH_MODEL, ResponseTemplate
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
    async def make_auth(cls):
        response = await post_request(cls.url, headers={}, body=cls.body)
        cookies = response.cookies

        with open("cookies.json", "w") as file:
            json.dump(dict(cookies), file)

    @classmethod
    async def get_profile(cls):
        with open("cookies.json", "r") as file:
            cookies = json.load(file)
        prof_url = f"{WEBLANCER_URL}{REQUEST_WL_PREFIX}/users/guest_1694859481282.json?login=guest_1694859481282"
        response = await get_request(prof_url, headers={}, cookies=cookies)
        profile = ResponseTemplate(**json.loads(response))
        return profile
