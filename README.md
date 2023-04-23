# ChatGPT Readme

This code sets up a chat interface that allows users to converse with OpenAI's GPT-3.5-Turbo language model. The conversation between the user and the model is saved to a log file, which is written to disk during the conversation. The log file contains a record of all messages exchanged during the conversation.

## Setup

To use this code, you need to set up an OpenAI API key and install the OpenAI python module. You can install the OpenAI python module using pip:

```shell
pip3 install openai
```

You also need to set the `OPENAI_API_KEY` environment variable to your API key. This can be done by running the following command in your terminal, replacing `YOUR_API_KEY` with your actual API key:

Alternatively, you can set the `OPENAI_API_KEY` environment variable in your operating system's environment variables.

```bash
export OPENAI_API_KEY=YOUR_API_KEY
```

## Usage

To run the chat interface, simply run the Python script from the command line:

```shell
python3 chat.py
```

or 

```shell
python3 chat4.py
```

Once the script is running, you will be prompted to enter your first message. Type your message and hit enter to start the conversation.

During the conversation, you can type "q" and hit enter to end the conversation and save the conversation log to disk. You can also type "p" and hit enter to save the conversation log to disk and start a new conversation.

## Notes

This code is designed to work with OpenAI's GPT-3.5-Turbo language model. If you want to use a different language model, you will need to modify the `model` parameter in the `openai.ChatCompletion.create()` function call.

This code saves the conversation log to a file in the `~/Projects/chatGPT/chats` directory. If you want to save the conversation log to a different directory, you will need to modify the `log_dir` variable in the code.
