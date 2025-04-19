import json
import requests

URL = "http://localhost:8000/summarize-chat"

with open("data/chat_logs/sample_chat_1.json", "r") as f:
    chat_data = json.load(f)

response = requests.post(URL, json=chat_data)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
