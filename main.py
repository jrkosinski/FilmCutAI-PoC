from source.classes.scene_splitter import SceneSplitter
from source.utils.encode_image import encode_frame_base64
#from LLM_LlavaLocal import LLM_LlavaLocal
import os

class DuplicatesList: 
    def __init__(self): 
        self.duplicates = {}

    def add(self, key, value): 
        if (key not in self.duplicates.keys()): 
            self.duplicates[key] = { }
        self.duplicates[key][value] = True
            
        #add the inverse as well 
        if (value not in self.duplicates.keys()): 
            self.duplicates[value] = { }
        self.duplicates[value][key] = True
        
    def are_duplicates(self, key1, key2): 
        return key1 in self.duplicates.keys() and key2 in self.duplicates.keys() and key1 in self.duplicates[key2].keys()

scene_splitter = SceneSplitter()
video_dir = "./scene_output/"
#scene_list = scene_splitter.find_scenes('./media/homevid.avi', write_out_scenes=True, output_dir=video_dir)
#print(scene_list)

duplicates = DuplicatesList()
checked_pairs = []
#llava = LLM_LlavaLocal("liuhaotian/llava-v1.5-7b")

def already_checked(f1, f2): 
    return "{0}:::{1}".format(f1, f2) in checked_pairs
    
def mark_checked(f1, f2): 
    checked_pairs.append("{0}:::{1}".format(f1, f2))
    checked_pairs.append("{0}:::{1}".format(f2, f1))


def do_these_videos_show_the_same_room(video_path1, video_path2): 
    #splice two videos together
    
    input = {
        'query': "do both halves of this video show the same room or part of the house? answer with Y for yes, N for no", 
        'videos': ["{0}--{1}".format(video_path1, video_path2)]
    }
    print(input.query)
    return True
    
    #llava.send({ query})


video_files = os.listdir(video_dir)
for file in video_files:
    print(file)
    for f in video_files: 
        if (f != file and not duplicates.are_duplicates(f, file) and not already_checked(file, f)): 
            if (do_these_videos_show_the_same_room(f, file)):
                duplicates.add(file, f)
            mark_checked(f, file)
            
print(duplicates)