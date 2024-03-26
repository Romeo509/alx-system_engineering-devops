#!/usr/bin/python3
"""
script that fetches info of all the emloyees
"""
import json
import requests


def fetch_users_data(base_url):
    """Fetches data about all employees."""
    users_url = f"{base_url}/users"

    response = requests.get(users_url)

    data = response.text

    return json.loads(data)


def export_to_json(builder):
    """Exports employee TODO tasks to a JSON file."""
    json_encoded_data = json.dumps(builder)
    with open("todo_all_employees.json", "w", encoding="UTF8") as myFile:
        myFile.write(json_encoded_data)


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users_data = fetch_users_data(base_url)

    builder = {}
    for user in users_data:
        user_id = str(user.get("id"))
        user_name = user.get("username")
        builder[user_id] = []

        tasks_url = f"{base_url}/todos?userId={user_id}"
        response = requests.get(tasks_url)
        tasks = json.loads(response.text)

        for task in tasks:
            json_data = {
                "task": task["title"],
                "completed": task["completed"],
                "username": user_name
            }
            builder[user_id].append(json_data)
    export_to_json(builder)

