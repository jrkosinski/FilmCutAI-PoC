import cv2

class VideoCap: 
    def __init__(self): 
        self.frames = []
        self.frame_rate = 0
        self.frame_width = 0
        self.frame_height = 0
        self.capture = None
        
    def frame_count(self): 
        return len(self.frames)
    
    def process(self, file_path, limit: int=0): 
        self.capture = cv2.VideoCapture(file_path)
        self.frames = []
        #success,image = vidcap.read()
        
        #detect framerate
        
        #detect frame size
        self.frame_width = int(self.capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.frame_rate = int(self.capture.get(cv2.CAP_PROP_FPS))

        success = True
        while success:
            success,image = self.capture.read()
            
            if (success): 
                self.frames.append(image)
                #cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
                
                if limit > 0 and len(self.frames) >= limit: 
                    break
                
        return self.frames
        
    #TODO: correct format
    def framesToVideo(self, frames, output_path, output_format = "mp4v"): 
        out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc('X','V','I','D'), self.frame_rate, (self.frame_width, self.frame_height))
        for frame in frames:
            out.write(frame)
        
    def release(self):
        if (self.capture is not None):
            self.capture.release()