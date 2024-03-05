import openai
import constants 
import os

os.environ["OPENAI_API_KEY"] = constants.APIKEY

messages = []
messages.append({"role": "system", "content": """
    You are a nutritionist who creates mealplans for patients 
    and gives nutritional guidance and advice"""})

print("What meal plan do you want to create? (Type 'quit' to exit)\n")
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
    
    print("What meal plan do you want to create? (Type 'quit' to exit)\n")
    
    


