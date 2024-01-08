from openai import OpenAI
import playsound
import os
from gtts import gTTS

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

messages = []

def question_answer(question, cumulative_messages, sound=True): 
    
    if (sound):
        audio = gTTS(text=question, lang="en", slow=False)
        audio.save("./mp3/question.mp3")
        playsound.playsound("./mp3/question.mp3")
    else:
        print(question)
    
    cumulative_messages.append(
        {
            "role": "user", 
            "content": question
        }
    )
    
    print('sending request...');
    completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=cumulative_messages
    )

    answer = completion.choices[0].message.content
    print(completion)
    print('')
    print(answer)
    
    cumulative_messages.append(
        {
            "role": "assistant", 
            "content": answer
        }
    )
    
    if (sound) :
        print('generating audio...')
        audio = gTTS(text=answer, lang="en", slow=False)
        
        print('saving audio...')
        audio.save("./mp3/answer.mp3")
        
        print('playing audio...')
        playsound.playsound("./mp3/answer.mp3")


