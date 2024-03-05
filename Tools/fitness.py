import openai
import constants 
import os

os.environ["OPENAI_API_KEY"] = constants.APIKEY

messages = []
messages.append({"role": "system", "content": 
    """You are a fitness coach specializing in kinesiology and 
    your job is to generate a fitness plan for clients based on 
    their individual goals."""})

print("What fitness plan do you want to create? (Type 'quit' to exit)\n")
while True:
    message = input("> ")
    if message == "quit":
        break
    
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
    
    print("What fitness plan do you want to create? (Type 'quit' to exit)\n")
    
    


