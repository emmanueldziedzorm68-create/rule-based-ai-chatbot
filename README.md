# Project 1: Rule-Based AI Chatbot

LogicBot is a Python terminal chatbot built around the Project 1 specification
on page 17 of the supplied training document. It uses predefined replies and
exact phrase matching. It needs Python 3 and no third-party packages.

## Run it

Open a terminal in this folder and run:

```powershell
python chatbot.py
```

Type `help` to see example messages. Type `bye`, `exit`, or `quit` to finish.
Ctrl+C or closing the input stream also ends the program politely.

## How it works

1. `input()` reads your message inside a continuous `while True` loop.
2. `normalise()` applies `.lower().strip()`, so `  HELLO  ` becomes `hello`.
3. An `if-else` decision checks for an exit command. An exit prints a goodbye
   and uses `break` to stop the loop.
4. Otherwise, `PHRASE_TO_INTENT` maps the exact cleaned phrase to an intent.
   An intent is the purpose of the message, such as greeting or asking for help.
5. `RESPONSES.get()` retrieves the predefined answer for that intent. An unknown
   phrase, including empty input, receives the fallback answer.
6. The program prints the reply and asks for another message.

The seven intents are greeting, wellbeing, identity, capabilities, explanation,
gratitude, and help. Exit commands are handled separately.

## Why dictionaries and conditionals are both used

Page 4 introduces `if-else` logic. Pages 12–15 explain how dictionaries can
replace a growing chain of response conditions, and page 17 specifically asks
for a dictionary with at least five intents. This implementation uses
conditionals for conversation control and dictionaries for response selection.
It demonstrates the progression without duplicating the chatbot.

## Example conversation

```text
LogicBot: Welcome! Type 'help' for examples or 'exit' to leave.
You:   HELLO
LogicBot: Hello! How can I help you? Type 'help' to see what I understand.
You: what is your name
LogicBot: I'm LogicBot, a simple rule-based chatbot.
You: tell me the weather
LogicBot: I don't understand that yet. Type 'help' to see the messages I recognise.
You: exit
LogicBot: Goodbye!
```

## Scope and limitations

This bot does not train a model, call an AI service, or use the Excel order
dataset. Those are unnecessary for the supplied Project 1 checklist.

Matching is exact after lowercasing and trimming surrounding whitespace.
Question-mark variants listed in the dictionary work; other punctuation,
misspellings, repeated internal spaces, and unlisted paraphrases receive the
fallback. The bot has no conversation memory and does not infer meaning.

To add a new topic, add an intent and reply to `RESPONSES`, then add supported
phrases mapped to that intent in `PHRASE_TO_INTENT`. Keep phrase keys lowercase
without surrounding whitespace.

## Verification

The implementation was checked for all seven intents, every listed phrase,
mixed case and surrounding whitespace, unknown and empty messages, repeated
conversation turns, all three exit commands, and end-of-input handling.
