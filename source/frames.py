import cv2
vidcap = cv2.VideoCapture('./media/home1.mp4')
#success,image = vidcap.read()
count = 0
success = True
while success:
  success,image = vidcap.read()
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  
  count += 1
  
  if count % 1000 == 0: 
      print(count)
  if count > 3: 
      break
  
print(count)