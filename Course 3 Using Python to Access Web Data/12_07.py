#Given http://py4e-data.dr-chuck.net/known_by_Aislinn.html
#Find the link at position 18 (the first name is 1). Follow that link. Repeat
#this process 7 times. The answer is the last name that you retrieve.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def url_parser(url):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    link_list = []
    for tag in tags:
        line = tag.get('href', None)
        link_list.append(line)
    url = link_list[position-1]
    return(url)

start_url = input('Enter URL:')
count = int(input('Enter count:'))
position = int(input('Enter position:'))

for i in range(1,count+2):
    print('Retrieving:',start_url)
    url_parser(start_url)
    start_url = url_parser(start_url)
