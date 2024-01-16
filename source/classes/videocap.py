import cv2

class VideoCap: 
    def __init__(self): 
        pass
    
    def toFrames(self, file_path, limit: int = 0): 
        capture = cv2.VideoCapture(file_path)
        frames = []
        #success,image = vidcap.read()

        success = True
        while success:
            success,image = capture.read()
            
            if (success): 
                imgdata = image.tobytes()
                frames.append(imgdata)
                #cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
                
                if limit > 0 and len(frames) >= limit: 
                    break
            
        return frames
        