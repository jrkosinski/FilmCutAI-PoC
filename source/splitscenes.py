from json import detect_encoding
from scenedetect.video_splitter import split_video_ffmpeg

scenes = []
split_video_ffmpeg(
    "./media/homevid.avi", 
    scenes,
    
)