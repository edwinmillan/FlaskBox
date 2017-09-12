import requests
import json


def lookup(host, content_type='json'):
    base_url = 'https://freegeoip.net'
    request_url = f'{base_url}/{content_type}/{host}'
    response = requests.get(request_url)
    return json.loads(response.content)
