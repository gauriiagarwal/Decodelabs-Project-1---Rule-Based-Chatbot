"""
DecodeLabs - AI Project 1: Rule-Based AI Chatbot
Architecture: IPO model (Input -> Process -> Output) inside an infinite loop.

Checklist from the spec:
  [x] INPUT LOOP      : continuous `while True`
  [x] SANITIZATION    : lower-case, strip whitespace (+ punctuation)
  [x] KNOWLEDGE BASE  : dictionary with 5+ intents
  [x] FALLBACK        : default reply via dict.get()
  [x] EXIT STRATEGY   : clean `break`
"""

import string

BOT_NAME = "DecoBot"

# ---------- KNOWLEDGE BASE (key -> value) ----------
KNOWLEDGE_BASE = {
    # greetings
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! Nice to meet you.",
    "hey": "Hey! What's up?",
    "good morning": "Good morning! Hope you have a great day.",
    "good evening": "Good evening! How can I help?",
    # small talk
    "how are you": "I'm just code, but I'm running perfectly. How about you?",
    "i am fine": "Glad to hear that!",
    "thanks": "You're welcome!",
    "thank you": "Happy to help!",
    # bot info
    "what is your name": f"I'm {BOT_NAME}, a rule-based chatbot.",
    "whats your name": f"I'm {BOT_NAME}, a rule-based chatbot.",
    "who made you": "I was built by an AI engineer at DecodeLabs (that's you!).",
    "what can you do": "I can greet you, answer a few AI questions, and chat until you say 'bye'.",
    "help": "Try: hello, how are you, what is ai, what is a chatbot, what is python, bye",
    # domain knowledge
    "what is ai": "AI (Artificial Intelligence) is making machines perform tasks that normally need human intelligence.",
    "what is a chatbot": "A chatbot is a program that simulates conversation with a user.",
    "what is rule based": "A rule-based system follows hard-coded if-else style rules, so it is predictable and traceable.",
    "what is python": "Python is a beginner-friendly, high-level programming language widely used in AI.",
}

EXIT_COMMANDS = {"bye", "exit", "quit", "goodbye", "see you"}

FALLBACK = "Sorry, I don't understand that yet. Type 'help' to see what I can answer."


# ---------- PHASE 1: INPUT & SANITIZATION ----------
def sanitize(raw_text: str) -> str:
    """Normalize user input so 'HELLO!!  ' and 'hello' match the same key."""
    text = raw_text.lower().strip()
    text = text.translate(str.maketrans("", "", string.punctuation))  # remove ? ! . ' etc.
    text = " ".join(text.split())  # collapse multiple spaces
    return text


# ---------- PHASE 2: PROCESS ----------
def get_response(clean_input: str) -> str:
    """Dictionary lookup + fallback in one atomic operation -> O(1)."""
    return KNOWLEDGE_BASE.get(clean_input, FALLBACK)


# ---------- PHASE 3: OUTPUT (the heartbeat loop) ----------
def main() -> None:
    print(f"{BOT_NAME}: Hello! I'm {BOT_NAME}. Type 'bye' to exit, 'help' for ideas.")

    while True:
        try:
            raw_input_text = input("You: ")
        except (EOFError, KeyboardInterrupt):  # Ctrl+D / Ctrl+C = clean exit
            print(f"\n{BOT_NAME}: Goodbye!")
            break

        clean_input = sanitize(raw_input_text)

        if clean_input == "":                    # user just pressed Enter
            print(f"{BOT_NAME}: Please type something.")
            continue

        if clean_input in EXIT_COMMANDS:         # KILL COMMAND
            print(f"{BOT_NAME}: Goodbye! Have a great day.")
            break

        print(f"{BOT_NAME}: {get_response(clean_input)}")


if __name__ == "__main__":
    main()