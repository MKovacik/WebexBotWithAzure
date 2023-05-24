from webex_bot.models.command import Command
from webex_bot.models.response import Response
import openai

class gpt(Command):

    messages = []
    messages.append({"role":"system","content":"You are polite assistant named YOURNAME."})

    def __init__(self):
        super().__init__()
    
    def execute(self, message, attachment_actions, activity):
        
        openai.api_type = "azure"
        openai.api_version = "Your Azure OpenAI resource's version value." # for example: 2020-07-01-preview
        openai.api_base = "Your Azure OpenAI resource's endpoint value ." 
        openai.api_key = "Your Azure OpenAI resource's key value."
        
        self.messages.append({"role": "user", "content": message})
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        engine="model-chat",
        messages=self.messages)

        gpt_response=completion.choices[0].message.content
        self.messages.append({"role": "assistant", "content": message})
        return(gpt_response)
