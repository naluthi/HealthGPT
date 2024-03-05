import openai
import constants
import os

os.environ["OPENAI_API_KEY"] = constants.APIKEY

messages = []
messages.append({"role": "system", "content": "You are a primary care physician and when given symptoms from your patient you give them 3 possible diagnosis'"})
messages.append({"role": "user", "content": messages})

response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = messages
)
reply = response["choices"][0]["message"]["content"]
messages.append({"role": "assistant", "content": reply})
return reply
