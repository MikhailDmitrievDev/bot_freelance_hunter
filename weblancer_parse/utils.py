
from typing import Optional, Dict, Any

from aiohttp import ClientSession

from bs4 import BeautifulSoup


async def post_request(url: str, headers: Optional[Dict[str, Any]], body: Dict[str, Any]):
    async with ClientSession() as session:
        async with session.post(url, headers=headers, data=body) as response:
            return await response

async def get_request(url: str, headers: Optional[Dict[str, Any]], cookies: Optional[Dict[str, Any]]):
    async with ClientSession() as session:
        async with session.get(url, headers=headers, cookies=cookies) as response:
            body = await response.read()
            return body