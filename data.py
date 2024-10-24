import requests 
import json
from keys import API_KEY

def lastfm_get(payload):
    headers = {'user-agent': 'user'}
    url  = 'https://ws.audioscrobbler.com/2.0/'

    payload['api_key'] = API_KEY
    payload['format'] = 'json'

    response = requests.get(url, headers=headers, params=payload)
    return response

def search_track(query:str):
    method = 'track.search'
    limit = 10
    payload = {
        'method': method, 
        'limit': limit, 
        'track': query
        } 
    results = lastfm_get(payload)

    data = results.json()['results']['trackmatches']['track']
    return data

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

if __name__ == '__main__':
    query =" duster inside out"
    results = search_track(query)
    
