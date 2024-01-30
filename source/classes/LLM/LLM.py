
import os


class LLM: 
    def __init__(self, model_name: str): 
        self.model_name = model_name
        self.history = []
    
    def send(self, input, append_history: bool, options=None): 
        pass
    
    def clear_history(self): 
        self.history = []


