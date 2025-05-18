from random import choice, randint
from reminder import *
from pomodoro import *
from todo import *
from calendar_function import *
from local_llm import *
from help import *

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == "-_-":
        return "Why are we still here? Just to suffer? \n...Or just to be quiet?"
    elif "hello there" in lowered:
        return "General Kenobi!"
    elif "hello" in lowered:
        return "Hi! How can I help you?"
    elif "roll dice" in lowered:
        return f"You rolled: {randint(1, 6)}"
    else:
        return choice(["I can't react to that yet.",
                       "Please try something else."])

