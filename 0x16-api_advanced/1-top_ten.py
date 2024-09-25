#!/usr/bin/python3
"""Module to query the Reddit API and print the titles of
the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts
    listed for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
    agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0)'
    agent += ' Gecko/20100101 Firefox/102.0'
    headers = {"user-Agent": agent}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
    else:
        resp = response.json().get('data').get('children')
        [print(res.get('data').get('title')) for res in resp]
