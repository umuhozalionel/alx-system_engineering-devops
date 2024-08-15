#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    results = response.json().get("data", {})
    return results.get("subscribers", 0)

# Obfuscation techniques
def _obfuscate_string(s):
    return ''.join(chr(ord(c) + 2) for c in s)

def _deobfuscate_string(s):
    return ''.join(chr(ord(c) - 2) for c in s)

def number_of_subscribers_obfuscated(subreddit):
    """Return the total number of subscribers on a given subreddit with obfuscation."""
    url = _deobfuscate_string("https://www.reddit.com/r/{}/about.json".format(subreddit))
    headers = {
        _deobfuscate_string("User-Agent"): _deobfuscate_string("linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)")
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    results = response.json().get(_deobfuscate_string("data"), {})
    return results.get(_deobfuscate_string("subscribers"), 0)
