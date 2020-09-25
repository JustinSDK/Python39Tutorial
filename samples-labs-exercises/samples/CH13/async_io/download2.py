from urllib.request import urlopen
import asyncio

async def load_url(url: str) -> bytes:
    with urlopen(url) as u:
        return u.read()

async def save(filename: str, content: bytes):
    with open(filename, 'wb') as f:
        f.write(content)

async def download(url: str, filename: str):
    content = await load_url(url)
    await save(filename, content)

async def main():
    urls = [
        'https://openhome.cc/Gossip/Encoding/',
        'https://openhome.cc/Gossip/Scala/',
        'https://openhome.cc/Gossip/JavaScript/',
        'https://openhome.cc/Gossip/Python/'
    ]

    filenames = [
        'Encoding.html',
        'Scala.html',
        'JavaScript.html',
        'Python.html'
    ]

    for url, filename in zip(urls, filenames):
        asyncio.create_task(download(url, filename))

asyncio.run(main())
    
