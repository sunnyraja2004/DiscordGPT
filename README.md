SunnyGPT Discord Bot 🤖

A Discord bot powered by Google Gemini (via google-generativeai) that can maintain conversational context and respond when mentioned in chat.
The bot loads a chat history file at startup, appends new messages as conversation progresses, and generates replies using Gemini models.

✨ Features

Connects to Discord using discord.py.

Uses Gemini 2.5 Flash Lite model for fast responses.

Maintains conversation context by storing messages in a rolling text log.

Responds only when mentioned (@SunnyGPT), avoiding unwanted chatter.

Configurable generation parameters: temperature, top-p, max tokens.

Supports multiple chat history files (chat1.txt, chat2.txt, chat3.txt).
⚙️ Requirements

Python 3.10+

discord.py

google-generativeai

Install dependencies:

pip install discord google-generativeai

🔑 Environment Variables

Set these before running:

Variable	Description
GEMINI_API_KEY	Your Google Gemini API key (from Google AI Studio).
SECRET_KEY	Your Discord bot token (from Discord Developer Portal).
