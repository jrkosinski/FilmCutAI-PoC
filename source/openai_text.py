from classes.llm import LLM_OpenAI

model = LLM_OpenAI()
response = model.send({
            "role": "user", 
            "content": "do you think they should make iphones for babies? answer in 10 words or fewer"
        })
        
print (response)