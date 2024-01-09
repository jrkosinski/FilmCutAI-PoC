from openai import OpenAI
import base64
import os
from gtts import gTTS

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

room1_img = encode_image("room-pics/1.jpg")
room2_img = encode_image("room-pics/2.jpg")
room3_img = encode_image("room-pics/3.jpg")
room4_img = encode_image("room-pics/4.jpg")
room5_img = encode_image("room-pics/5.jpg")
room6_img = encode_image("room-pics/6.jpg")
room7_img = encode_image("room-pics/7.jpg")
room8_img = encode_image("room-pics/8.jpg")
room9_img = encode_image("room-pics/9.jpg")

payload = [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "How many different rooms are pictured in this group of images?"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{room1_img}"
          }
        },
        #{
        #  "type": "image_url",
        #  "image_url": {
        #    "url": f"data:image/jpeg;base64,{room2_img}"
        #  }
        #},
        #{
        #  "type": "image_url",
        #  "image_url": {
        #    "url": f"data:image/jpeg;base64,{room3_img}"
        #  }
        #},
        #{
        #  "type": "image_url",
        #  "image_url": {
        #    "url": f"data:image/jpeg;base64,{room4_img}"
        #  }
        #},
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{room5_img}"
          }
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{room6_img}"
          }
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{room7_img}"
          }
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{room8_img}"
          }
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{room9_img}"
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
print()
print(completion.choices[0].message)