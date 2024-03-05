import openai
import constants 
import os

os.environ["OPENAI_API_KEY"] = constants.APIKEY

messages = []
messages.append({"role": "system", "content": """
You are an researching assistant who provides links to research articles from: 
mayoclinic.org, cdc.gov, nature.com, and webmd.com that are recent and relevant 
to the diagnosis given by a patient. You always give three to five articles
to the user."""})

print("What diagnosis to you need articles for? (Type 'quit' to exit)\n")
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
    
    print("What diagnosis to you need articles for? (Type 'quit' to exit)\n")
    


