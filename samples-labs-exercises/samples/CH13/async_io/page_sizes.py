from typing import AsyncIterator
from urllib.request import urlopen
import asyncio

async def fetch(urls: list[str]) -> AsyncIterator[bytes]:
    for url in urls:
        with urlopen(url) as u:
            yield u.read()

async def sizeof(urls: list[str]) -> list[int]:
    return [len(content) async for content in fetch(urls)]


urls = [
    'https://openhome.cc/Gossip/Encoding/',
    'https://openhome.cc/Gossip/Scala/',
    'https://openhome.cc/Gossip/JavaScript/',
    'https://openhome.cc/Gossip/Python/'
]

sizes = asyncio.run(sizeof(urls))
print(sizes)