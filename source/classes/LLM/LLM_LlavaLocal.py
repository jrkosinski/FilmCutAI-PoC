from LLM import LLM
import torch
from videollava.constants import IMAGE_TOKEN_INDEX, DEFAULT_IMAGE_TOKEN
from videollava.conversation import conv_templates, SeparatorStyle
from videollava.model.builder import load_pretrained_model
from videollava.utils import disable_torch_init
from videollava.mm_utils import tokenizer_image_token, get_model_name_from_path, KeywordsStoppingCriteria

class LLM_LlavaApi (LLM): 
    def __init__(self, model_path):
        LLM.__init__(self, model_path)
        self.tokenizer = None
        self.model = None
        self.processor = None
        
        load_4bit, load_8bit = True, False
        model_name = get_model_name_from_path(model_path)
        cache_dir = 'cache_dir' 
        device = 'cuda' 
        tokenizer, model, processor, _ = load_pretrained_model(model_path, None, model_name, load_8bit, load_4bit, device=device, cache_dir=cache_dir)
        
        self.tokenizer = tokenizer
        self.model = model
        self.processor = processor
    
    def send(self, input, append_history: bool, options=None): 
        disable_torch_init()
        
        video = input.video
        query = input.query
        conv_mode = "llava_v1"  #could be options 
        video_processor = self.processor['video']  #could be options 
        
        conv = conv_templates[conv_mode].copy()
        roles = conv.roles

        video_tensor = video_processor(video, return_tensors='pt')['pixel_values']
        if type(video_tensor) is list:
            tensor = [video.to(self.model.device, dtype=torch.float16) for video in video_tensor]
        else:
            tensor = video_tensor.to(self.model.device, dtype=torch.float16)

        print(f"{roles[1]}: {query}")
        query = ' '.join([DEFAULT_IMAGE_TOKEN] * self.model.get_video_tower().config.num_frames) + '\n' + query
        conv.append_message(conv.roles[0], query)
        conv.append_message(conv.roles[1], None)
        prompt = conv.get_prompt()
        input_ids = tokenizer_image_token(prompt, self.tokenizer, IMAGE_TOKEN_INDEX, return_tensors='pt').unsqueeze(0).cuda()
        stop_str = conv.sep if conv.sep_style != SeparatorStyle.TWO else conv.sep2
        keywords = [stop_str]
        stopping_criteria = KeywordsStoppingCriteria(keywords, self.tokenizer, input_ids)

        with torch.inference_mode():
            output_ids = self.model.generate(
                input_ids,
                images=tensor,
                do_sample=True,
                temperature=0.1,
                max_new_tokens=1024,
                use_cache=True,
                stopping_criteria=[stopping_criteria])

        outputs = self.tokenizer.decode(output_ids[0, input_ids.shape[1]:]).strip()
        print(outputs)
