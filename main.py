from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import *


load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")


intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

#msg functionality
async def send_message(message: Message, user_message: str) -> None:
    if message.author == client.user:
        return

    if not user_message:
        print("Message was empty (probably intents not enabled properly)")
        return

    is_private = user_message[0] == '?'
    if is_private:
        user_message = user_message[1:]

    try:
        await message.author.send(user_message) if is_private else await message.channel.send(user_message)
    except Exception as e:
        print(e)

@client.event
async def on_ready() -> None:
    print(f"{client.user} is now running!")

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    command = None
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    for text in ["/miniai", "/ai", "/reminder", "/pomodoro", "/todo"]:
        if message.content.startswith(text):
            command = message.content.split(" ")[0]
            user_message = message.content.replace(text, "")
            print("Yes, it was a command!")


    if command == "/help" or command == "/h":
        pass
    elif command == "/miniai" or command == "/ai":
        bot_response = local_llm_response(prompt=user_message)
        await send_message(message, bot_response)
    elif command == "/reminder":
        #   /reminder <time> <message>
        #   /reminder 20m 15s "What the dog doing?"
        response = reminder(user_message, message)
        await send_message(message, response)
    elif command == "/pomodoro":
        #   /pomodoro <work_time> <break_time> <repeats>
        #   /reminder 20m 15s 1h 1m 1s 5
        response = await pomodoro(user_message, message)
        await send_message(message, response)
    elif command == "/todo":
        #   /pomodoro <work_time> <break_time> <repeats>
        #   /reminder 20m 15s 1h 1m 1s 5
        response = todo(user_message, message.author.id)
        await send_message(message, response)
    else:
        print(f"[{channel}] {username}: {user_message}")
        response = get_response(user_message)
        await send_message(message, response)

def main() -> None:
    client.run(TOKEN)

if __name__ == "__main__":
    main()