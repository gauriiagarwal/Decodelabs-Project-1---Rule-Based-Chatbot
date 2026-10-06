# 🤖 Rule-Based AI Chatbot

> **DecodeLabs · AI Industrial Training Kit · Project 1 (Batch 2026)**
> A deterministic, "white-box" chatbot built with pure Python control flow: no ML, no APIs, no hallucinations.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Type](https://img.shields.io/badge/Type-Rule--Based%20AI-purple)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 About

This project is the foundation phase of the DecodeLabs AI track. Before building systems that *learn*, you must master systems that follow **explicit logic**. The chatbot reads user input, cleans it, looks it up in a knowledge base, and replies, all inside a continuous loop that only stops on an exit command.

Two versions are included:

| File | Description |
|---|---|
| `chatbot.py` | **Basic version**: clean, minimal implementation of the project spec |
| `chatbot_creative.py` | **Creative version "Nova"**: personality, colors, typing effect, memory, quiz and more |

---

## ✅ Project Requirements Covered

| Requirement | Implementation |
|---|---|
| Input loop: continuous `while` cycle | `while True:` in `main()` |
| Sanitization: handle case & whitespace | `sanitize()` → `.lower().strip()` + punctuation removal |
| Knowledge base: dictionary with 5+ intents | `KNOWLEDGE_BASE` / `INTENTS` dictionaries |
| Fallback: default response for unknowns | `dict.get(key, FALLBACK)` |
| Exit strategy: clean break command | `bye`, `exit`, `quit` → `break` |

---

## 🧠 How It Works (IPO Model)

```
   INPUT                    PROCESS                      OUTPUT
┌──────────┐   ┌────────────────────────────┐   ┌──────────────────┐
│ raw text │ → │ sanitize → dictionary look │ → │ print the reply  │
│ "HELLO!" │   │ up (O(1)) → fallback      │   │ and loop again   │
└──────────┘   └────────────────────────────┘   └──────────────────┘
        ▲                                                │
        └────────────────── while True ◄─────────────────┘
```

**Why a dictionary instead of an `if-elif` ladder?**
An `if-elif` chain checks rules one by one → **O(n)**. A dictionary jumps straight to the answer → **O(1)**, no matter how many rules you add. `dict.get()` handles lookup and fallback in a single step.

---

## ✨ Features

### Basic version (`chatbot.py`)
- Greetings, small talk and AI/Python Q&A
- Input sanitization (`"  HELLO!!  "` → `"hello"`)
- Default reply for unknown input
- Empty-input handling and safe exit (also on `Ctrl+C`)

### Creative version (`chatbot_creative.py`)
- 🎭 Personality ("Nova") with random replies per intent
- ⌨️ Typing effect and colored terminal output
- 🧾 Remembers your name (`my name is ...`)
- 🧠 Mini quiz (3 random AI/Python questions with score)
- 💬 Mood check-in (nested, multi-turn conversation)
- 🎲 Jokes, quotes, coin flip, dice, current time/date
- 🇮🇳 Hinglish triggers (`namaste`, `kaise ho`, `hasao`, `tata`)
- 🔍 Word-by-word matching, so `"tell me a joke"` works too

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher ([download](https://www.python.org/downloads/))
- No external libraries needed. Only the Python standard library is used.

### Installation

```bash
git clone https://github.com/<your-username>/rule-based-chatbot.git
cd rule-based-chatbot
```

### Run

```bash
# Basic version
python chatbot.py

# Creative version
python chatbot_creative.py
```

> **Windows tip:** if `python` isn't recognized, use `py chatbot.py` instead.

---

## 💬 Sample Conversation

```
DecoBot: Hello! I'm DecoBot. Type 'bye' to exit, 'help' for ideas.
You: HELLO!!
DecoBot: Hi there! How can I help you today?
You: What is AI?
DecoBot: AI (Artificial Intelligence) is making machines perform tasks that normally need human intelligence.
You: asdf
DecoBot: Sorry, I don't understand that yet. Type 'help' to see what I can answer.
You: bye
DecoBot: Goodbye! Have a great day.
```

**Creative version**

```
You > my name is Gauri
Nova > Nice to meet you, Gauri! I'll remember it until you close me 😉
You > mood
Nova > Mood check-in! How are you feeling? (happy / sad / stressed / bored / tired)
You > stressed
Nova > Breathe in for 4, hold for 4, out for 4. One task at a time - you've got this 🧘
```

---

## 📁 Project Structure

```
rule-based-chatbot/
├── chatbot.py            # Basic rule-based chatbot (project spec)
├── chatbot_creative.py   # Creative "Nova" edition
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🛠️ Customization

- **Add a new rule:** add a key/value pair to `KNOWLEDGE_BASE` in `chatbot.py`, or a new entry in `INTENTS` in `chatbot_creative.py`.
- **Change the personality:** edit `BOT` and the reply lists.
- **Add quiz questions:** append `(question, {accepted answers})` to the `QUIZ` list.

---

## 🔮 Future Improvements

- [ ] **Hybrid architecture:** rule match → instant reply; no match → pass to an LLM (rules as guardrails)
- [ ] Fuzzy matching for typos (e.g., `difflib`)
- [ ] Persistent memory (save user name/history to a JSON file)
- [ ] Simple GUI with Tkinter or a web UI with Streamlit
- [ ] Semantic matching with embeddings (leads into Project 2: from keys to vectors)

---

## 📚 What I Learned

- Control flow and decision-making logic
- Input sanitization and normalization
- Why hash maps beat `if-elif` ladders (O(1) vs O(n))
- Designing with the Input → Process → Output model
- Why deterministic rule layers matter as guardrails around generative AI

---

## 👩‍💻 Author

**Gauri Agarwal**
B.Tech Electronics Engineering (VLSI Design & Technology), Banasthali Vidyapith


- LinkedIn: https://www.linkedin.com/in/gauri-agarwal-a7821a301

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<p align="center">Built as part of the <b>DecodeLabs AI Industrial Training Kit</b> 🚀</p>
