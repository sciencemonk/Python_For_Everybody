# Using beautiful soup to parse web pages

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url:')
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retreive all of the anchor tags
tags = soup('a')
count = 0
links = []
for tag in tags:
    line = tag.get('href', None)
    if line.startswith('https://') or line.startswith('http://'):
        count += 1
        links.append(line)

for i in links:
    print(i)
print('Total links:', count)

