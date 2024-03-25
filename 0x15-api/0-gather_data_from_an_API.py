#!/usr/bin/python3
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetching user data
    user_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )
    todo_response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )

    if user_response.status_code != 200:
        print("Error: Employee data not found")
        sys.exit(1)
    if todo_response.status_code != 200:
        print("Error: TODO data not found")
        sys.exit(1)

    user_data = user_response.json()
    todo_data = todo_response.json()

    # Filter completed tasks
    completed_tasks = [task for task in todo_data if task['completed']]

    # Displaying results
    print((
        f"Employee {user_data['name']} is done with tasks"
        f"({len(completed_tasks)}/{len(todo_data)}):"
    ))

    for task in completed_tasks:
        print(f"\t {task['title']}")
