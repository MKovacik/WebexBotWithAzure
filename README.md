# WebexBotWithAzure

This project enables the creation of a Webex bot that utilizes a ChatGPT instance hosted in Azure Open AI Studio. The entire project can be deployed within an Azure Web App.

## Requirements

1. Webex account
2. Azure account with access to Azure Open AI Studio

## Setup Guide

### Creating a Bot for Webex

1. Navigate to [Webex for Developers](https://developer.webex.com/my-apps).
2. Create a new bot as per the instructions in the [Webex Bot documentation](https://developer.webex.com/docs/bots#creating-a-webex-bot).
3. Add the created bot's token to `app.py`.

### Setting Up a GPT Instance in Azure

1. Follow the instructions in this [Azure ChatGPT Quickstart Guide](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/chatgpt-quickstart?pivots=rest-api&tabs=command-line) to create a new ChatGPT instance.
2. Update the `openai.api_base` in `gpt.py` with the Endpoint.
3. Add either Key 1 or Key 2 to `openai.api_key` in `gpt.py`.
4. It's recommended to store these keys as environment variables for security purposes.

### Creating an Azure Web App

1. Create an Azure Web App following this [Azure Python Web App Quickstart Guide](https://learn.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=flask%2Cwindows%2Cazure-cli%2Cvscode-deploy%2Cdeploy-instructions-azportal%2Cterminal-bash%2Cdeploy-instructions-zip-azcli).
2. This project includes a ready-to-use `requirements.txt` file. You can fork this project, update `app.py` and use your repository for deployment.
3. Enable "Always On" in your application settings.
4. Ensure 'python app.py' is set as the Startup command.

Now, you can interact with your bot on Webex and start chatting! Enjoy!

## Inspiration
- [Collabcrush's ChatGPT on GitHub](https://github.com/collabcrush/chatgpt)

## What's Next?

For future enhancements and ideas, you can refer to this project: [fbradyirl's Webex Bot on GitHub](https://github.com/fbradyirl/webex_bot)
