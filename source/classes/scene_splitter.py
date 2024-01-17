from scenedetect import SceneManager
from scenedetect.detectors import ContentDetector
from scenedetect import detect, AdaptiveDetector, split_video_ffmpeg
import cv2

class SceneSplitter: 
    def __init__(self): 
        pass

    def find_scenes(self, video_path, output_dir='./', write_out_scenes=False, threshold=30.0):
        scene_list = detect(video_path, AdaptiveDetector())
        if (output_dir is None or len(output_dir) == 0): 
            output_dir = "./"
        if not output_dir.endswith("/"): 
            output_dir += "/"
            
        if (write_out_scenes): 
            split_video_ffmpeg(video_path, scene_list)
        return scene_list

