#!/usr/bin/python3
"""Fetches employee's information and TODO list from a REST API."""
import json
import requests
import sys

base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":
    """Script to fetch employee info and their TODO list from an API."""
    employee_id = sys.argv[1]

    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    user_name = user_data['name']

    tasks_url = f"{base_url}/todos?userId={employee_id}"
    tasks_response = requests.get(tasks_url)
    tasks_data = tasks_response.json()

    completed_tasks = [task for task in tasks_data if task['completed']]

    print(
         f"Employee {user_name} is done with tasks "
        f"({len(completed_tasks)}/{len(tasks_data)}):"
    )
    for task in completed_tasks:
        print(f"\t{task['title']}")
