import openai
import constants 
import os

os.environ["OPENAI_API_KEY"] = constants.APIKEY

messages = []
messages.append({"role": "system", "content": 
    """You are a primary care physician and when given 
    symptoms from your patient you give them 5 treatments 
    they can do at home to help until they are able to see a doctor"""})


print("What symtoms are you experiencing and need treatment for? (Type 'quit' to exit)\n")
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
    
    print("What symtoms are you experiencing and need treatment for? (Type 'quit' to exit)\n")
    
    


