# Discord Virtual Assistant Bot

A simple but powerful Discord bot written in Python that acts as your personal assistant. It integrates with your local LLM, Google Calendar, and provides handy productivity tools like reminders, a Pomodoro timer, and a to-do list.

---

## Features

* Ask questions from a local LLM
* Create and list Google Calendar events
* Set reminders
* Run Pomodoro timers
* Maintain a to-do list

---

## Commands

```
/miniai <prompt>` or `/ai <prompt>
    • You can ask the bot anything using the local LLM

/calendar list <x>
    • Lists your next 'n' Google Calendar events
    • e.g. /calendar list 5

/calendar add "<title>" <start> <end>
    • Creates an event in your Google Calendar with the given title
    • e.g. /calendar add "Meet Bob" 2025-05-10T10:00:00 2025-05-10T10:30:00

/reminder <time> "<message>"
    • Gives you a reminder with the message after the time given
    • e.g. /reminder 1h 15m "Stretch your legs"

/pomodoro <work> <break> <cycles>
    • Runs a Pomodoro timer for the amount of cycles given
    • e.g. /pomodoro 25m 5m 4

/todo list
    • Shows all the tasks on your to-do list

/todo add <task>
    • Adds the task to your to-do list
    • e.g. /todo add Finish report

/todo done <#>
    • Removes a task by its number
    • e.g. /todo done 2

/help
    • Shows the help message with all commands
```

---