#!/usr/bin/python3
"""Module to give the count of subscriber for a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """GET Reddit subscriber count"""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscribers = data.get('data', {}).get('subscribers', 0)
            return subscribers
        else:
            return 0
    except requests.RequestException:
        return 0
