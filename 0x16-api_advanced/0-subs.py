#!/usr/bin/python3
"""Module to give the count of subscriber for a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """GET Reddit subscriber count"""

    headers = {'User-agent': 'alx-system_engineering-devops-0x16-api_advanced'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    with requests.get(url, allow_redirects=False, headers=headers) as resp:
        is_success = resp.ok
        response = resp.json()

    if not is_success:
        return 0

    return response.get("data").get("subscribers")


if __name__ == "__main__":
    subreddit = sys.argv[1]
    number_of_subscribers(subreddit)
