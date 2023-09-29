#!/usr/bin/python3
"""Python script to export data in the JSON format
"""
import json
import requests


def fetch_all_employee_todo_data():
    # Define the API endpoint URL
    base_url = 'https://jsonplaceholder.typicode.com'
    users_url = f'{base_url}/users'
    todos_url = f'{base_url}/todos'

    # Make GET requests to fetch user and TODO list data
    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    # Check if the requests were successful
    if users_response.status_code != 200:
        return
    if todos_response.status_code != 200:
        return

    # Parse JSON responses
    users_data = users_response.json()
    todos_data = todos_response.json()

    # Create a dictionary to store the JSON data
    json_data = {}

    # Populate the JSON data
    for user in users_data:
        user_id = str(user['id'])
        if user_id not in json_data:
            json_data[user_id] = []

        # Find tasks for the current user
        user_tasks = [task for task in todos_data if
                      task['userId'] == user['id']]

        # Populate the user's tasks in the JSON data
        for task in user_tasks:
            task_data = {
                "username": user['username'],
                "task": task['title'],
                "completed": task['completed']
            }
            json_data[user_id].append(task_data)

    # Create a JSON file for all employees
    json_filename = 'todo_all_employees.json'

    # Write JSON data to the file
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    fetch_all_employee_todo_data()
