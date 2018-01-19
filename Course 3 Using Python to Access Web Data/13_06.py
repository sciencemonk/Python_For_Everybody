import urllib.request, urllib.parse, urllib.error
import json

user_url = input('Enter location: ')
print('Retrieving', user_url)
file_handler = urllib.request.urlopen(user_url)
data = file_handler.read().decode()

info = json.loads(data)

count = 0
count_sum = 0
for item in info["comments"]:
    print(item['count'])
    count += 1
    count_sum += item['count']

print('Count:',count)
print('Sum:',count_sum)
