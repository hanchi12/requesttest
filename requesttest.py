import urllib.parse
import requests
import json

main_api = 'http://maps.googleapis.com/maps/api/geocode/json?'

address='lhr'
url=main_api+urllib.parse.urlencode({'address':'san jose'})

json_data = requests.get(url).json()

print('requesting...')
print(json_data)