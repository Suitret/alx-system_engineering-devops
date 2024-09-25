#!/usr/bin/python3
"""Module to query the Reddit API and print the titles of
the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts
    listed for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:124.0)'
    agent += ' Gecko/20100101 Firefox/124.0'
    headers = {'User-Agent': agent}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print("None")
        return
    result = response.json().get("data").get("children")
    for post in result:
        print(post.get("data").get("title"))
