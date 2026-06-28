#!/usr/bin/python3
"""Script that returns information about an employee's TODO list progress"""
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    ).json()
    employee_name = user["name"]

    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    ).json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task["completed"]]
    number_done = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_done, total_tasks))
    for task in done_tasks:
        print("\t {}".format(task["title"]))
