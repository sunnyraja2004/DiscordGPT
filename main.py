# app id: 1120362291678953643
# public key: 8b91abc5972092ae66d90386785d48adec67551cebb8f10216052237ed5fe923 

import discord
import os
import google.generativeai as genai

# --- Step 1: Configure the API Key ---
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY environment variable not set.")
    exit()
genai.configure(api_key=api_key)

# --- FIX #1: Initialize the Modern Gemini Model ---
# Create an instance of the GenerativeModel. It's best to do this once
# when the script starts, not on every message.
# We also create a configuration object for generation parameters.
generation_config = genai.GenerationConfig(
    temperature=0.9,
    top_p=1.0,
    max_output_tokens=256,
)
model = genai.GenerativeModel(
    model_name='gemini-2.5-flash-lite',
    generation_config=generation_config
)


# Load the initial chat context
file = "1"
match(file):
  case "1":
    file = "chat1.txt"
  case "2":
    file = "chat2.txt"
  case "3":
    file = "chat3.txt"
  case _:
    print("Invalid choice.")
    exit()

with open(file, "r") as f:
  chat = f.read()

# Load the Discord bot token
token = os.getenv("SECRET_KEY")
if not token:
    print("Error: SECRET_KEY environment variable not set.")
    exit()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        global chat
        try:
            # Prevent the bot from replying to its own messages
            if self.user == message.author:
                return

            chat += f"{message.author.display_name}: {message.content}\n"
            print(f'Message from {message.author}: {message.content}')

            if self.user in message.mentions:
                # --- FIX #2: Use the new `generate_content` method ---
                # This is the correct function for the model instance.
                # The prompt is now the first argument.
                response = model.generate_content(f"{chat}\nSunnyGPT: ")

                channel = message.channel

                # --- FIX #3: Access the response text via `.text` ---
                # The generated text is now in the `.text` attribute of the response.
                messageToSend = response.text

                # Update the chat history with the bot's own message
                chat += f"SunnyGPT: {messageToSend}\n"

                await channel.send(messageToSend)

        except Exception as e:
            print(f"An error occurred: {e}")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)