import requests

url = "http://localhost:11434/api/generate"
payload = {"model": "mistral", "prompt": "Hello", "stream": False}

try:
    response = requests.post(url, json=payload)
    print(f"Response Status: {response.status_code}")
    print(f"Response Text: {response.text}")
except Exception as e:
    print(f"Request failed: {e}")
