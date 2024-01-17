from source.classes.videocap import VideoCap
from source.classes.llm import LLM_OpenAI_Vision
from source.utils.encode_image import encode_frame_base64

cap = VideoCap()
cap.process('./media/home1.mp4')
frames = cap.frames

print(cap.frame_width)
print(cap.frame_height)
print(cap.frame_rate)
print(cap.frame_count())


print(len(frames))
llm = LLM_OpenAI_Vision();
image1 = frames[198]
image2 = frames[200]
imgdata1 = encode_frame_base64(image1)
imgdata2 = encode_frame_base64(image2)

subframes = []
for i in range (10, 30): 
    subframes.append(frames[i])
cap.framesToVideo(subframes, "./subframes.mp4")

'''
answer = llm.send({
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Do you think that these images are taken in the same room?"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{imgdata1}"
          }
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{imgdata2}"
          }
        }
      ]
})

print(answer)
'''