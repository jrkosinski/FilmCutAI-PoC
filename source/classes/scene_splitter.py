from scenedetect import SceneManager
from scenedetect.detectors import ContentDetector
from scenedetect import detect, AdaptiveDetector, split_video_ffmpeg
import os, shutil

class SceneSplitter: 
    def __init__(self): 
        pass

    def find_scenes(self, video_path, output_dir='./', write_out_scenes=False, threshold=30.0):
        scene_list = detect(video_path, AdaptiveDetector())
        if (output_dir is None or len(output_dir) == 0): 
            output_dir = "./"
        if not output_dir.endswith("/"): 
            output_dir += "/"
            
        #write scenes to files
        if (write_out_scenes): 
            split_video_ffmpeg(video_path, scene_list)
        
        #afterwards, move files to the appropriate directory
        if (output_dir != "./"): 
            
            #clear directory first
            self._clear_output_dir(output_dir)
            
            files = os.listdir()
            for filename in files: 
                #TODO: have to account for different formats
                if (filename.endswith(".mp4") and filename.find("-Scene-") >= 0): 
                    os.replace("./{0}".format(filename), "{0}{1}".format(output_dir, filename))
                
            return scene_list

    def _clear_output_dir(self, output_dir): 
        for filename in os.listdir(output_dir):
            file_path = os.path.join(output_dir, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))