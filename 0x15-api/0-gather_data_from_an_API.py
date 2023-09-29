#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


def fetch_employee_todo_progress(employee_id):
    # Define the API endpoint URL
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    # Make GET requests to fetch user and TODO list data
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    # Check if the requests were successful
    if user_response.status_code != 200:
        return
    if todos_response.status_code != 200:
        return

    # Parse JSON responses
    user_data = user_response.json()
    todos_data = todos_response.json()

    # Calculate the number of completed tasks
    completed_tasks = [task for task in todos_data if task['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos_data)

    # Display employee TODO list progress
    print(f"Employee {user_data['name']} is done with \
            tasks({num_completed_tasks}/{total_tasks}):")

    # Display titles of completed tasks
    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_employee_todo_progress(employee_id)
