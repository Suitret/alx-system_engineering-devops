#!/usr/bin/python3
"""Python script to export data in the JSON format
"""
import json
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

    # Create a dictionary to store the JSON data
    json_data = {str(user_data['id']): []}

    # Populate the JSON data
    for task in todos_data:
        task_data = {
            "task": task['title'],
            "completed": task['completed'],
            "username": user_data['username']
        }
        json_data[str(user_data['id'])].append(task_data)

    # Create a JSON file with the user's ID as the filename
    json_filename = f'{employee_id}.json'

    # Write JSON data to the file
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_employee_todo_progress(employee_id)
