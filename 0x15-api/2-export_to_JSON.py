#!/usr/bin/python3
"""
function to fetch info about a given employee with
an api into json
"""
import json
import requests
import sys


def fetch_user_info(user_id):
    """Fetches user information from the API."""
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users?id={user_id}'
    response = requests.get(user_url)
    data = response.json()
    user_name = data[0].get('username')
    return user_name


def export_to_json(user_id, user_name):
    """Exports user TODO tasks to a JSON file."""
    base_url = 'https://jsonplaceholder.typicode.com'
    tasks_url = f'{base_url}/todos?userId={user_id}'
    response = requests.get(tasks_url)
    tasks = response.json()
    dict_key = str(user_id)
    builder = {dict_key: []}
    for task in tasks:
        json_data = {
            "task": task['title'],
            "completed": task['completed'],
            "username": user_name
        }
        builder[dict_key].append(json_data)
    json_encoded_data = json.dumps(builder)
    with open(f'{user_id}.json', 'w', encoding='UTF8') as myFile:
        myFile.write(json_encoded_data)


if __name__ == "__main__":
    user_id = sys.argv[1]
    user_name = fetch_user_info(user_id)
    export_to_json(user_id, user_name)
