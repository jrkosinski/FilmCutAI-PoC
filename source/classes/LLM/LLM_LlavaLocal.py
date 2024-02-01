from LLM import LLM

import sys
sys.path.append('../../../')

from llava.model.builder import load_pretrained_model
from llava.mm_utils import get_model_name_from_path
from llava.eval.run_llava import eval_model


class LLM_LlavaLocal (LLM): 
    def __init__(self, model_name):
        LLM.__init__(self, model_name)
    
    def send(self, input, append_history: bool, options=None): 
        pass
    