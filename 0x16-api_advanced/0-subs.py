#!/usr/bin/python3
"subscribers count"

import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 404:
        return 0
    
    try:
        data = response.json()
        return data['data']['subscribers']
    except ValueError:
        print("Response content is not valid JSON")
        return 0

