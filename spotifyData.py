import json
from pprint import pprint

data_file =  open('spotifyData.json')
data = json.load(data_file)
for item in data['items']:
    print(item['track']['name'])
