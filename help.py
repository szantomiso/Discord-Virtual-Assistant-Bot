def help_handler() -> str:
    return (
        "**Here are all the commands you can use:**\n\n"
        "`/miniai <prompt>` or `/ai <prompt>`\n"
        "\t• You can ask the bot anything using the local LLM\n\n"
        "`/calendar list <x>`\n"
        "\t• Lists your next  \'n\'  Google Calendar events\n"
        "\t• e.g. `/calendar list 5`\n\n"
        "`/calendar add \"<title>\" <start> <end>`\n"
        "\t• Creates an event in your Google Calendar with the given title\n"
        "\t• e.g. `/calendar add \"Meet Bob\" 2025-05-10T10:00:00 2025-05-10T10:30:00`\n\n"
        "`/reminder <time> \"<message>\"`\n"
        "\t• Gives you a reminder with the message after the time given\n"
        "\t• e.g. `/reminder 1h 15m \"Stretch your legs\"`\n\n"
        "`/pomodoro <work> <break> <cycles>`\n"
        "\t• Runs a Pomodoro timer for the amount of cycles given\n"
        "\t• e.g. `/pomodoro 25m 5m 4`\n\n"
        "`/todo list`\n"
        "\t• Shows all the tasks on your to-do list\n\n"
        "`/todo add <task>`\n"
        "\t• Adds the task to your to-do list\n"
        "\t• e.g. `/todo add Finish report`\n\n"
        "`/todo done <#>`\n"
        "\t• Removes a task by its number\n"
        "\t• e.g. `/todo done 2`\n\n"
        "`/help` or `/h`\n"
        "\t• Shows this help message\n"
    )