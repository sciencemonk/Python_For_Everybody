#Scraping numbers from HTML using BeautifulSoup

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url:')
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

count = 0
tags = soup('span')
for tag in tags:
    count += int(tag.contents[0])

print('Sum:',count)
