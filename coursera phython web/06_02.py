import urllib.request,urllib.parse,urllib.error
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter address: ')
    if len(address)<1: break
    url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})

    uh = urllib.request.urlopen(url)
    data = uh.read().decode()

    js = json.loads(data)

    place_id = js['results'],[0],['place_id']
    print(place_id)