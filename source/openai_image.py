from openai import OpenAI
import base64
import os
from gtts import gTTS

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
    
base64_image = encode_image("frame0.jpg")

payload = [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What's in this image?"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ]


completion = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=payload, 
    max_tokens=300
)

print(completion)