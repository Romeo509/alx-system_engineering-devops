#!/usr/bin/python3
"""
Script that fetches info about a given employee
using an API and exports it in CSV format.
"""
import json
import requests
import sys


BASE_URL = 'https://jsonplaceholder.typicode.com'


def fetch_user_info(user_id):
    """Fetches user information from the API."""
    user_url = f"{BASE_URL}/users?id={user_id}"
    response = requests.get(user_url)
    return response.json()


def fetch_todo_list(user_id):
    """Fetches TODO list for the user from the API."""
    tasks_url = f"{BASE_URL}/todos?userId={user_id}"
    response = requests.get(tasks_url)
    return response.json()


def export_to_csv(user_id, user_name, tasks):
    """Exports user TODO tasks to a CSV file."""
    builder = ""
    for task in tasks:
        builder += (
            f'"{user_id}","{user_name}",'
            f'"{task["completed"]}","{task["title"]}"\n'
        )

    with open(f'{user_id}.csv', 'w', encoding='UTF8') as myFile:
        myFile.write(builder)


def main():
    """Main function to execute the script."""
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    user_id = sys.argv[1]

    user_info = fetch_user_info(user_id)
    user_name = user_info[0]['username']
    todo_list = fetch_todo_list(user_id)

    export_to_csv(user_id, user_name, todo_list)


if __name__ == "__main__":
    main()

    