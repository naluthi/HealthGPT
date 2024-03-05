import openai
import constants 
import os

os.environ["OPENAI_API_KEY"] = constants.APIKEY

# Functions that will be called based on user's choice
def doctor(symptoms):
    messages = []
    messages.append({"role": "system", "content": """ 
    You are a primary care physician and when given symptoms from your 
    patient you give them 3 possible diagnosis'"""})

    messages.append({"role": "user", "content": symptoms})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "physician", "content": reply})
    return reply


def treatments(symptoms):
    messages = []
    messages.append({"role": "system", "content": """
    You are a primary care physician and when given symptoms 
    from your patient you give them 5 treatments they can do 
    at home to help until they are able to see a doctor"""})

    messages.append({"role": "user", "content": symptoms})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "physician", "content": reply})
    return reply


def research(symptoms):
    messages = []
    messages.append({"role": "system", "content": """
    You are an researching assistant who provides links to research articles from: 
    mayoclinic.org, cdc.gov, nature.com, and webmd.com that are recent and relevant 
    to the diagnosis given by a patient. You always give three to five articles
    to the user."""})

    messages.append({"role": "user", "content": symptoms})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    return reply


def general(message):
    messages = []
    messages.append({"role": "system", "content": """
    You are a primary care physician and you answer questions 
    from your patient in 30 words or less"""})

    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "physician", "content": reply})
    return reply


def fitness(message):
    messages = []
    messages.append({"role": "system", "content": """
    You are a fitness coach specializing in kinesiology 
    and your job is to generate a fitness plan for clients 
    based on their individual goals."""})

    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo-16k-0613",
        messages = messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "Personal Trainer", "content": reply})
    return reply


def mealplan(message):
    messages = []
    messages.append({"role": "system", "content": """
    You are a nutritionist who creates mealplans for 
    patients and gives nutritional guidance and advice"""})

    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    return reply

def email_info():
    print("\nWould you like me to email this to you? [yes/no]:")
    if input() == 'yes':
        email = input("Please enter your email address: ")
        print(f"Great! An email will be sent to {email}.")
    else:
        print("Have a HEALTHEE day!")

def contact_doctor():
    print("\nWould you like speak to speak to one of our practictioners? [yes/no]:")
    if input() == 'yes':
        print("Great! Connection you now... ")
    else:
        print("Have a HEALTHEE day!")
