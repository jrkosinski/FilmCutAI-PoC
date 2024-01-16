from source.classes.videocap import VideoCap
from source.classes.llm import LLM_OpenAI


cap = VideoCap()
frames = cap.toFrames('./media/home1.mp4', 3) 
print(len(frames))

