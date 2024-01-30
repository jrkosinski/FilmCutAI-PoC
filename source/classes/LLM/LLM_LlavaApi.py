from LLM import LLM

class LLM_LlavaApi (LLM): 
    def __init__(self, model_name):
        LLM.__init__(self, model_name)
    
    def send(self, input, append_history: bool, options=None): 
        pass
    