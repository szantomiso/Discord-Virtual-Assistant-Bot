import asyncio
import re

def reminder(user_input, message) -> str:
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