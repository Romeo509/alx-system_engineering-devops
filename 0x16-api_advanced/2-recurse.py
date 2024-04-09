#!/usr/bin/python3
"""
Queries the Reddit API recursively and returns a list
containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API for hot articles in a subreddit.

    Args:
        subreddit (str): The subreddit to search.
        hot_list (list): List to store titles of hot articles.

    Returns:
        list: Titles of all hot articles, or None if subreddit is invalid.
    """
    headers = {'User-Agent': 'MyBot/1.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100}  # Request up to 100 posts per page
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            hot_list.append(post['data']['title'])

        if data['data']['after'] is not None:
            return recurse(subreddit, hot_list=hot_list)
        else:
            return hot_list
    else:
        return None
