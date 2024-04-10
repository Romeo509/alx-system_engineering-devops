#!/usr/bin/python3
"""Count words in Reddit titles"""

import requests


def count_words(subreddit, word_list, after="", counts=[]):
    """Count occurrences of words from word_list in Reddit titles"""

    if after == "":
        counts = [0] * len(word_list)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'user-agent': 'CustomUserAgent'}

    response = requests.get(url, params={'after': after}, headers=headers,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        for topic in data['data']['children']:
            for word in topic['data']['title'].split():
                for i, target_word in enumerate(word_list):
                    if target_word.lower() == word.lower():
                        counts[i] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for i, word in enumerate(word_list):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        save.append(j)
                        counts[i] += counts[j]

            for i in range(len(word_list)):
                for j in range(i, len(word_list)):
                    if (counts[j] > counts[i] or
                            (word_list[i] > word_list[j] and
                             counts[j] == counts[i])):
                        counts[i], counts[j] = counts[j], counts[i]
                        word_list[i], word_list[j] = word_list[j], word_list[i]

            for i, word in enumerate(word_list):
                if counts[i] > 0 and i not in save:
                    print(f"{word.lower()}: {counts[i]}")
        else:
            count_words(subreddit, word_list, after, counts)
