#!/usr/bin/python3
"""Module to give the count of subscriber for a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Function to give the count of subscriber for a subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid being blocked by Reddit's API
    headers = {
        'User-Agent':
        'python:subreddit.subscriber.counter:v1.0.0 (by /u/Mental_Way_8071)'
    }

    # Make a GET request to the Reddit API
    response = requests.get(url, headers=headers,
                            allow_redirects=False)

    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
