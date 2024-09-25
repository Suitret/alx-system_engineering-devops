#!/usr/bin/python3
"""Module to query the Reddit API and print the titles of
the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts
    listed for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)

        # Ensure that the response has a status code 200 (OK)
        if response.status_code == 200:
            try:
                data = response.json()  # Attempt to parse JSON
                posts = data.get('data').get('children')

                # If there are no posts, handle it gracefully
                if not posts:
                    print(None)
                    return

                for post in posts:
                    print(post.get('data').get('title'))
            except ValueError:
                print(None)
        else:
            print(None)
    except requests.RequestException as e:
        print(None)
