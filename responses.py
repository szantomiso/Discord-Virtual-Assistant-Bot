from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == "":
        return "Why are we still here? Just to suffer? Or just to be quiet?"
    elif "hello" in lowered:
        return "Hi! How can I help you?"
    elif "hello there" in lowered:
        return "General Kenobi"
    elif "roll dice" in lowered:
        return f"You rolled: {randint(1, 6)}"
    else:
        return choice(["I can't react to that yet.",
                       "The F*CK you say to me?!",
                       "Please try something else."])