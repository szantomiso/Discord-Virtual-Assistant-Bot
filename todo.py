import os
import json

TODO_FILE="todo_data.json"

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return {}

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=4)

def todo(user_input, user_id):
    todos = load_todos()
    user_id_str = str(user_id)
    user_tasks = todos.get(user_id_str, [])

    args = user_input.strip().split(" ", 1)
    if not args:
        return "Invalid format. Please use: /todo [add / list / done]"

    command = args[0].lower()

    if command == "add":
        if len(args) < 2:
            return "Please provide a task to add."
        task = args[1].strip()
        user_tasks.append(task)
        todos[user_id_str] = user_tasks
        save_todos(todos)

        return f"Task added: '{task}'"

    elif command == "list":
        if not user_tasks:
            return "You don't have any tasks yet."

        tasks = " \n"

        for i, task in enumerate(user_tasks):
            tasks += f"{i+1}. {task}\n"

        return tasks

    elif command == "done" or command == "remove":
        if len(args) < 2:
            return "Please provide the number of the task to remove."

        try:
            index = int(args[1]) - 1
        except Exception as e:
            print(e)
            return "Please provide a valid number of the task to remove."

        if 0 <= index < len(user_tasks):
            removed = user_tasks.pop(index)
            todos[user_id_str] = user_tasks
            save_todos(todos)
            return f"Task removed: {removed}"
        else:
            return "Invalid task number."
    else:
        return "Invalid format. Please use: /todo add <task> or /todo list or /todo done <index of task>."