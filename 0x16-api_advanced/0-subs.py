#!/usr/bin/python3
"""Module to give the count of subreddits
"""
import requests
from requests.auth import HTTPBasicAuth


client_id = 'iABR_GeVfRaPZJJDIPcXng'
client_secret = 'x30M5_WNFaH7EWSRFswOwMhab5cqFg'


def number_of_subscribers(subreddit):
    """Set up the API URL for the subreddit's information
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid being blocked by Reddit's API
    headers = {
        'User-Agent':
        'python:subreddit.subscriber.counter:v1.0.0 (by /u/Mental_Way_8071)'
    }

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers,
                                auth=HTTPBasicAuth(client_id, client_secret),
                                allow_redirects=False)

        # Check if the status code is 200 (OK)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Return the number of subscribers
            return data['data']['subscribers']
        else:
            return 0

    except requests.RequestException as e:
        return 0
