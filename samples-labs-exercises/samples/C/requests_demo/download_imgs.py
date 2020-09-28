from bs4 import BeautifulSoup
import requests

def save(content, filename):
    with open(filename, 'wb') as dest:
        dest.write(content)

def download(urls):
    for url in urls:
        resp = requests.get(url, stream=True)
        filename = url.split('/')[-1]
        save(resp.raw.read(), filename)

def download_imgs_from(url):
    resp = requests.get(url)
    resp.encoding = 'UTF-8'
    soup = BeautifulSoup(resp.text, 'html.parser')
    imgs = soup.find_all('img')
    srcs = (img.get('src') for img in imgs)
    download(f'{url}/{src}' for src in srcs)

download_imgs_from('https://openhome.cc/Gossip')
