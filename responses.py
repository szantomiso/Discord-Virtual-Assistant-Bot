from random import choice, randint
import requests
import re
import asyncio

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

def reminder(user_input, message):
#   1h 12m 15s "Feed the thing :["
#   20m "What the dog doing?"
    time_pattern = r"(?:(\d+)\s*h)?\s*(?:(\d+)\s*m)?\s*(?:(\d+)\s*s)?\s*\"(.+?)\""
    match = re.match(time_pattern, user_input)

    if not match:
        return "Invalid format. Please use: `/reminder 1h 2m 3s \"Your message\"`"

    hours = int(match.group(1)) if match.group(1) else 0
    minutes = int(match.group(2)) if match.group(2) else 0
    seconds = int(match.group(3)) if match.group(3) else 0
    reminder_msg = match.group(4)

    total_seconds = hours * 3600 + minutes * 60 + seconds
    print(total_seconds)
    if total_seconds <= 0:
        return "Time must be greater than 0."


    async def reminder_task():
        await asyncio.sleep(total_seconds)
        await message.channel.send(f"Reminder: {reminder_msg}")


    asyncio.create_task(reminder_task())

    if hours == 0:
        hoursString = ""
    elif hours == 1:
        hoursString = f"{hours} hour"
    else:
        hoursString = f"{hours} hours"

    if minutes == 0:
        minutesString = ""
    elif hours == 1:
        minutesString = f"{minutes} minute"
    else:
        minutesString = f"{minutes} minutes"

    if seconds == 0:
        secondsString = ""
    elif hours == 1:
        secondsString = f"{seconds} second"
    else:
        secondsString = f"{seconds} seconds"

    return f"Reminder set for {hoursString} {minutesString} {secondsString}!"