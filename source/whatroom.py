from openai import OpenAI
import base64
import os
from gtts import gTTS

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

content = [
        {
          "type": "text",
          "text": "How many different rooms are pictured in this group of images?"
        }
      ]
  
for n in range(1, 13): 
    img = encode_image("./media/room-pics/" + str(n) + ".jpg")
    content.append({
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{img}"
          }
    })
      
payload = [
    {
      "role": "user",
      "content": content
    }
  ]


completion = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=payload, 
    max_tokens=300
)

#print(completion)
print()
print(completion.choices[0].message)
print()