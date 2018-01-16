# Using beautiful soup to parse web pages

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter url:')
html = urllib.request.urlopen(url).read()
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
