"""
TASK 1: CHATBOT WITH RULE-BASED RESPONSES

A beginner-friendly chatbot that matches words and phrases in a user's
message and responds using predefined rules. No external packages needed.
"""

import random
import re
from datetime import datetime


RESPONSES = {
    "greeting": [
        "Hello! How can I help you today?",
        "Hi there! What would you like to talk about?",
        "Hey! Nice to meet you."
    ],
    "how_are_you": [
        "I'm doing well, thanks for asking! How are you?",
        "I'm just a program, but I'm ready to help!"
    ],
    "name": [
        "I'm RuleBot, a simple rule-based chatbot.",
        "You can call me RuleBot!"
    ],
    "thanks": [
        "You're welcome!",
        "Happy to help!",
        "No problem. Is there anything else?"
    ],
    "goodbye": [
        "Goodbye! Have a great day.",
        "See you later. Take care!"
    ],
    "study": [
        "Try studying in short focused sessions and take regular breaks.",
        "A useful approach is to understand a topic, practise it, and then revise it."
    ],
    "technology": [
        "Technology uses scientific knowledge to solve practical problems.",
        "Programming, databases, networking, and cybersecurity are important areas of technology."
    ],
    "help": [
        "You can ask me about greetings, my name, studies, technology, or how I am doing."
    ]
}


def classify_message(message: str) -> str:
    """Return the category that best matches the user's message."""
    text = message.lower().strip()

    if re.search(r"\b(hello|hi|hey|good morning|good afternoon|good evening)\b", text):
        return "greeting"
    if re.search(r"\b(how are you|how's it going|how are things)\b", text):
        return "how_are_you"
    if re.search(r"\b(your name|who are you|what are you called)\b", text):
        return "name"
    if re.search(r"\b(thank you|thanks|thx)\b", text):
        return "thanks"
    if re.search(r"\b(study|exam|learning|revision| 공부)\b", text):
        return "study"
    if re.search(r"\b(technology|computer|programming|coding|software|database)\b", text):
        return "technology"
    if re.search(r"\b(help|options|what can you do)\b", text):
        return "help"
    if re.search(r"\b(bye|goodbye|exit|quit)\b", text):
        return "goodbye"

    return "unknown"


def get_response(message: str) -> str:
    """Generate a response using the predefined rules."""
    category = classify_message(message)

    if category == "unknown":
        return (
            "I'm not sure I understood that. Try asking about studies, "
            "technology, or type 'help' to see what I can answer."
        )

    return random.choice(RESPONSES[category])


def main() -> None:
    print("=" * 54)
    print("             RULE-BASED CHATBOT")
    print("=" * 54)
    print("RuleBot: Hello! I am RuleBot. Type 'help' for topics.")
    print("RuleBot: Type 'bye' or 'exit' whenever you want to stop.")

    while True:
        try:
            user_message = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nRuleBot: Goodbye!")
            break

        if not user_message:
            print("RuleBot: Please enter a message.")
            continue

        response = get_response(user_message)
        print(f"RuleBot: {response}")

        if classify_message(user_message) == "goodbye":
            break


if __name__ == "__main__":
    main()
