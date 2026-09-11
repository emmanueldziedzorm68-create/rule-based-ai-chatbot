"""Project 1: a rule-based chatbot using exact matches and a dictionary."""

# Each key represents a distinct intent (the purpose of a user's message).
RESPONSES = {
    "greeting": "Hello! How can I help you? Type 'help' to see what I understand.",
    "wellbeing": "I'm ready to chat. Thanks for asking!",
    "identity": "I'm LogicBot, a simple rule-based chatbot.",
    "capabilities": "I can greet you, introduce myself, explain how I work, and respond to thanks.",
    "explanation": "I match your cleaned message to predefined rules. I don't learn or generate new answers.",
    "gratitude": "You're welcome!",
    "help": "Try: hello, how are you, what is your name, what can you do, how do you work, or thanks. Type bye, exit, or quit to leave.",
}

# Multiple exact phrases can express the same intent.
PHRASE_TO_INTENT = {
    "hello": "greeting",
    "hi": "greeting",
    "hey": "greeting",
    "how are you": "wellbeing",
    "how are you?": "wellbeing",
    "what is your name": "identity",
    "what is your name?": "identity",
    "who are you": "identity",
    "who are you?": "identity",
    "what can you do": "capabilities",
    "what can you do?": "capabilities",
    "how do you work": "explanation",
    "how do you work?": "explanation",
    "thanks": "gratitude",
    "thank you": "gratitude",
    "help": "help",
}

EXIT_COMMANDS = {"bye", "exit", "quit"}
FALLBACK = "I don't understand that yet. Type 'help' to see the messages I recognise."


def normalise(message):
    """Ignore letter case and whitespace at either end of the message."""
    return message.lower().strip()


def get_response(clean_message):
    """Look up a normalised phrase, then return its reply or the fallback."""
    intent = PHRASE_TO_INTENT.get(clean_message)
    return RESPONSES.get(intent, FALLBACK)


def main():
    print("LogicBot: Welcome! Type 'help' for examples or 'exit' to leave.")

    while True:
        try:
            message = normalise(input("You: "))
        except (EOFError, KeyboardInterrupt):
            # Also finish politely if input closes or the user presses Ctrl+C.
            print("\nLogicBot: Goodbye!")
            break

        if message in EXIT_COMMANDS:
            print("LogicBot: Goodbye!")
            break
        else:
            print("LogicBot:", get_response(message))


if __name__ == "__main__":
    main()
