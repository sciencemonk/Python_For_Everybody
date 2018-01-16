import xml.etree.ElementTree as ET
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location:')
print('Retrieving', url)
xml_data = urlopen(url, context=ctx).read()

tree = ET.fromstring(xml_data)
xml_list = tree.findall('comments/comment')
int_list = []
count = 0
char_count = 0

for item in xml_list:
    int_string = item.find('count').text
    char_count += len(item)
    int_list.append(int(int_string))
    count += 1

print('Retrieved',char_count,'characters')
print('Count:',count)
print('Sum:',sum(int_list))
