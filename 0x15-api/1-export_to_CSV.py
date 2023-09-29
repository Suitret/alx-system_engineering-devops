#!/usr/bin/python3
"""Python script to export data in the CSV format
"""
import csv
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

    # Create a CSV file with the user's ID as the filename
    csv_filename = f'{employee_id}.csv'

    # Write CSV data
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)

        # Write header row
        csv_writer.writerow(["USER_ID", "USERNAME",
                            "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write data rows
        for task in todos_data:
            csv_writer.writerow([user_data['id'], user_data['username'],
                                task['completed'], task['title']])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_employee_todo_progress(employee_id)
