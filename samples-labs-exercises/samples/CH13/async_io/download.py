from urllib.request import urlopen
import asyncio

async def download(url: str, file: str):
    with urlopen(url) as u, open(file, 'wb') as f:
        f.write(u.read())

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
