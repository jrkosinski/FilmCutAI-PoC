from openai import OpenAI
import os

class LLM: 
    def __init__(self, model_name: str): 
        self.model_name = model_name
        self.history = []
    
    def send(self, input, append_history: bool, options=None): 
        pass
    
    def clear_history(self): 
        self.history = []


class LLM_Llava (LLM): 
    def __init__(self, model_name):
        LLM.__init__(self, model_name)
    
    def send(self, input, append_history: bool, options=None): 
        pass
    

class LLM_OpenAI (LLM): 
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
        
        return completion.choices[0].message.content
            

