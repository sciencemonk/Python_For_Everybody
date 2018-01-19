#The program will prompt for a location, contact a web service and retrieve JSON
#for the web service and parse that data, and retrieve the first place_id from
#the JSON. A place ID is a textual identifier that uniquely identifies a place
#as within Google Maps.

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

address = input('Enter location: ')
url = serviceurl + urllib.parse.urlencode(
    {'address': address})

file_handler = urllib.request.urlopen(url)
data = file_handler.read().decode()
info = json.loads(data)

print(info['results'][0]['place_id'])
