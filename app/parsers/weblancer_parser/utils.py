
from typing import Optional, Dict, Any

from aiohttp import ClientSession

from bs4 import BeautifulSoup


async def post_request(url: str, headers: Optional[Dict[str, Any]], body: Dict[str, Any]):
    async with ClientSession() as session:
        async with session.post(url, headers=headers, data=body) as response:
            status_code = response.status
            cookies = response.cookies
            body = await response.text()
            return {'status_code': status_code, 'body': body, 'cookies': cookies}


async def get_request(url: str, headers: Optional[Dict[str, Any]], cookies: Optional[Dict[str, Any]] = None):
    async with ClientSession() as session:
        async with session.get(url, headers=headers, cookies=cookies) as response:
            status_code = response.status
            cookies = response.cookies
            body = await response.text()
            return {'status_code': status_code, 'body': body, 'cookies': cookies}
