import openai
import os
from datetime import datetime
import logging

# Set up authentication
openai.api_key = os.environ["OPENAI_API_KEY"]

# Set up logging
agent = "Tim"
log_dir = "chats"
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"chat_log_{timestamp}.txt"
file_path = os.path.join(os.getcwd(), log_dir, filename)

logging.basicConfig(
    filename=file_path,
    level=logging.INFO,
    format="%(asctime)s\n%(message)s"
)

# Define function to generate response from GPT
def generate_response_from_GPT(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"{prompt}"}
            ],
            temperature=0.7,
            max_tokens=2000,
            n=1,
            stop=None
        )

        message = response.choices[0].message.content.strip()

        print(f"\n{agent}:\n{message}\n\n---")
        logging.info(f"User:\n{prompt}\n\n{agent}:\n{message}\n\n---")

        return True
    except openai.error as e:
        print(f"Error calling OpenAI API: {str(e)}")
        return False

def end_conversation():
    print("Leaving Chat...")

def quit_issued(prompt):
    if prompt.lower() == "q":
        end_conversation()
        return True

# Get initial prompt from user
prompt = input("Beginning Chat...\n\nYou:\n")

# Start conversation loop
try:
    while True:
        # Process user input
        if not generate_response_from_GPT(prompt):
            break

        # Get new prompt from user
        prompt = input("Enter a new prompt (or 'q' to quit):\n")

        if quit_issued(prompt):
            break
except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    logging.info("End of conversation")
