from random import choice, randint
import requests
from reminder import *
from pomodoro import *
from todo import *

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == "-_-":
        return "Why are we still here? Just to suffer? Or just to be quiet?"
    elif "hello there" in lowered:
        return "General Kenobi!"
    elif "hello" in lowered:
        return "Hi! How can I help you?"
    elif "roll dice" in lowered:
        return f"You rolled: {randint(1, 6)}"
    else:
        return choice(["I can't react to that yet.",
                       "Please try something else."])

#llama model needed
def local_llm_response(prompt):
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

