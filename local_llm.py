import requests

def local_llm_response(prompt) -> str:
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return f"AAAAAAAAHHHHHHHHH: {response.status_code} - {response.text}"

