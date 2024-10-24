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

def write(data, file_name = 'output'):
    with open(f'{file_name}.json', 'w', encoding ='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent = 4)


def display(results):
    for result in results:
        print(result)

if __name__ == '__main__':
    query =" duster inside out"
    results = search_track(query)
    write(results)
    
