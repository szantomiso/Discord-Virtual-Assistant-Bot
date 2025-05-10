import re
import asyncio

def parse_time_string(time_str):
    matches = re.findall(r"(\d+)\s*(h|m|s)", time_str)
    total_seconds = 0
    for value, unit in matches:
        value = int(value)
        if unit == 'h':
            total_seconds += value * 3600
        elif unit == 'm':
            total_seconds += value * 60
        elif unit == 's':
            total_seconds += value
    return total_seconds

async def pomodoro(user_input: str, message):
    try:
        parts = user_input.strip().split()
        if len(parts) < 3:
            return "Invalid format. Please use: /pomodoro <work_time> <break_time> <repeats> (e.g. /pomodoro 25m 5m 3)"

        loops = int(parts[-1])
        time_parts = parts[:-1]

        half = len(time_parts) // 2
        work_time_str = ' '.join(time_parts[:half])
        break_time_str = ' '.join(time_parts[half:])

        work_time = parse_time_string(work_time_str)
        break_time = parse_time_string(break_time_str)

        if work_time == 0 or break_time == 0 or loops <= 0:
            return "Invalid time or loop count."

        await message.channel.send(f"Pomodoro started: {loops} cycles of {work_time_str} of work time and {break_time_str} of break time.")

        for i in range(loops):
            await asyncio.sleep(work_time)
            await message.channel.send(f"Work session no.{i + 1} done! \nStarting break timer...")

            await asyncio.sleep(break_time)
            if i == loops - 1:
                await message.channel.send(f"Break no. {i + 1} done!")
            else:
                await message.channel.send(f"Break no. {i + 1} done! \nStarting work timer...")

        await message.channel.send("Pomodoro timer done!")

        return None

    except Exception as e:
        print(e)
        return "Something went wrong in pomodoro timer."
