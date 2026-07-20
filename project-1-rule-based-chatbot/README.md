# Rule-Based AI Chatbot

A simple rule-based chatbot built in Python as Project 1 for the AI Internship track at Decode Labs. This project focuses on foundational control flow and decision-making logic before moving into more advanced AI concepts.

## What It Does

The chatbot runs in a continuous loop, takes user input, and matches it against a set of predefined phrases to generate a response. If the input doesn't match anything known, it falls back to a default message instead of crashing.

## Features

- **Continuous input loop** — keeps the conversation going until the user exits
- **Input sanitization** — normalizes user input (lowercase + whitespace trimming) so `HELLO`, `hello`, and `  hello  ` are all treated the same
- **Dictionary-based response matching** — uses a dictionary with `.get()` instead of long if-elif chains
- **Graceful fallback** — unrecognized inputs get a default reply instead of an error
- **Clean exit** — typing `bye` or `exit` ends the chat properly

## Why Dictionary Instead of If-Elif?

A common beginner approach is to chain many `if/elif` statements to match user input. This works, but doesn't scale well — every new phrase adds more lines, and Python has to check each condition one by one from top to bottom.

Using a dictionary with `.get()` solves this: Python can look up any key directly, regardless of how many phrases exist, making the code both cleaner and more efficient as it grows.

```python
responses = {
    "hello": "Hi there!",
    "bye": "Goodbye!"
}
reply = responses.get(clean_input, "I don't understand that.")
```

## Example Conversation

You: HELLO
Bot: Hi there!
You: how are you
Bot: I am doing great!
You: thanks
Bot: You are welcome!
You: bye
Bot: Goodbye!

## Tech Used

- Python 3.12
- No external libraries — pure Python control flow and dictionaries

## How to Run

```bash
python chatbot.py
```

## What's Next

Future iterations could expand the response set, add nested conditions for more nuanced replies, or introduce basic personality/tone variation.