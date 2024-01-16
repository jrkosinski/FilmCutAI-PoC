from classes.llm import LLM_OpenAI
from utils.encode_image import encode_image_base64

model = LLM_OpenAI(model_name="gpt-4-vision-preview")
image_data = encode_image_base64("./frame0.jpg")
response = model.send({
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What's in this image?"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{image_data}"
          }
        }
      ]
    })
        
print (response)