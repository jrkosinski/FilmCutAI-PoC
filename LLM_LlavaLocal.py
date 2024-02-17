from source.classes.LLM import LLM

import torch
from videollava.constants import IMAGE_TOKEN_INDEX, DEFAULT_IMAGE_TOKEN
from videollava.conversation import conv_templates, SeparatorStyle
from videollava.model.builder import load_pretrained_model
from videollava.utils import disable_torch_init
from videollava.mm_utils import tokenizer_image_token, get_model_name_from_path, KeywordsStoppingCriteria

from source.classes.videocap import VideoCap

class LLM_LlavaLocal (LLM): 
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
    
    def send(self, input, append_history: bool=False, options=None): 
        disable_torch_init()
        
        video_filepath1 = input.videos[0]
        query = input.query
        conv_mode = "llava_v1"  #could be options 
        video_processor = self.processor['video']  #could be options 
        
        conv = conv_templates[conv_mode].copy()
        roles = conv.roles

        video_tensor1 = video_processor(video_filepath1, return_tensors='pt')['pixel_values']
        
        if type(video_tensor1) is list:
            tensor = [video.to(self.model.device, dtype=torch.float16) for video in video_tensor1]
        else:
            tensor = video_tensor1.to(self.model.device, dtype=torch.float16)

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
                temperature=0.001,
                max_new_tokens=1024,
                use_cache=True,
                stopping_criteria=[stopping_criteria])

        outputs = self.tokenizer.decode(output_ids[0, input_ids.shape[1]:]).strip()
        print(outputs)
        #TODO: return only part of the output 
        return outputs


class LLavaInput: 
    def __init__(self, query = "", videos = []): 
        self.videos = videos
        self.query = query

#TODO: move these to a llava-utils file 
def do_these_videos_show_the_same_room(video_path1, video_path2): 
    #splice two videos together
    output_path = "{0}--{1}".format(os.path.basename(video_path1), os.path.basename(video_path2)); 
    VideoCap.splice_videos(video_path1, video_path2, output_path=output_path)
    
    input = LLavaInput(
        query="do both halves of this video show the same room or part of the house? answer with Y for yes, N for no, ONLY please.", 
        videos = [output_path]
    )

    print(input.query)
    
    #llava.send(input)
    return True
    
def is_exterior_shot(video_path): 
    input = LLavaInput(
        query="does this video show primarily an exterior of a house (as opposed to an interior)? Answer with Y for yes, N for no, ONLY please.", 
        videos = [video_path]
    )
    print(input.query)
    
    #llava.send(input)
    return True
    