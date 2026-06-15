import requests

API_URL = "http://localhost:8000"

def get_tasks():
    response = requests.get(f"{API_URL}/tasks")

    if response.status_code == 200:
        return response.json()

    return []

def create_task(title, description):
    payload = {
        "title": title,
        "description": description
    }

    response = requests.post(f"{API_URL}/tasks", json=payload)

    return response

def delete_task(task_id):
    response = requests.delete(f"{API_URL}/tasks/{task_id}")

    return response

def change_task_status(task_id, status):
    payload = {
        "is_completed": status
    }
    response = requests.put(f"{API_URL}/tasks/{task_id}/status", json=payload)

    return response