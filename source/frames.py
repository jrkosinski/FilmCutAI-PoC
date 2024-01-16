from classes.videocap import VideoCap

cap = VideoCap()
frames = cap.toFrames('./media/home1.mp4', 3) 
print(len(frames))
