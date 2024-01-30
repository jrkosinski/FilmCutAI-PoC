from LLM import LLM
import os
from openai import OpenAI

class LLM_OpenAiApi (LLM): 
    def __init__(self, model_name = "gpt-4-1106-preview"):
        LLM.__init__(self, model_name)
        self.client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    
    def send(self, input, append_history: bool = True, options=None): 
        messages = []
        if (append_history): 
            messages = self.history
        
        messages.append(input)
        
        #send request
        completion = self.client.chat.completions.create(
            model=self.model_name, #"gpt-4-1106-preview",
            messages=messages
        )
        
        print(completion.choices)
        return completion.choices[0].message.content
            

class LLM_OpenAiApi_Vision (LLM_OpenAiApi): 
    def __init__(self):
        LLM_OpenAiApi.__init__(self, "gpt-4-vision-preview")
    
            