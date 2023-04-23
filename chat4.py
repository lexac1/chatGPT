# Developed from the following prompt in chatGPT 4

# I am looking to develop a chatGPT api python3 app. It will be issued from the mac terminal, and have the following functionality:

# 1. It will call the openai python client chat feature
# 2. It should use the gpt-3.5-turbo model
# 3. It should print the chat to the screen
# 4. It should log with the python logging package, the prompt, agent name, and response.
# 5. You should be able to declare your agent name and the ai's name in the file which will be used in the logging and print messages to the screen.
# 6. The formatting of the print to screen and log file should be identical
# 7. The log file should be named with a timestamp in the file name and the file should be created in a subfolder "chats" in the current working directory.
# 8. You should be able to exit the conversation by entering "q" as the prompt with out making another request to the api.
# 9. There should be error handling around the api and the conversation.

import openai
import logging
import os
from datetime import datetime

# Set up authentication
openai.api_key = os.environ["OPENAI_API_KEY"]

# Set up agent names
your_agent_name = "User"
ai_agent_name = "ChatGPT"

# Set up logging
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
log_file = f"chats/chat_log_{timestamp}.log"

if not os.path.exists("chats"):
    os.makedirs("chats")

logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s\n%(message)s')

def log_and_print(agent_name, message):
    formatted_message = f"{agent_name}: {message}"
    print(formatted_message)
    logging.info(formatted_message)

def chat(prompt):
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.8,
        )
        message = response.choices[0].text.strip()
        return message
    except Exception as e:
        log_and_print("Error", f"An error occurred: {e}")
        return None

def main():
    log_and_print("Info", "Starting chat session...")

    while True:
        user_input = input(f"{your_agent_name}: ")

        if user_input.lower() == "q":
            log_and_print("Info", "Ending chat session...")
            break

        log_and_print(your_agent_name, user_input)
        ai_response = chat(user_input)

        if ai_response is not None:
            log_and_print(ai_agent_name, ai_response)

if __name__ == "__main__":
    main()
