import os
import constants
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

os.environ["OPENAI_API_KEY"] = constants.APIKEY

# 1. Vectorise the diagnostic csv data
loader = CSVLoader(file_path="all_diets.csv")
documents = loader.load()

embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(documents, embeddings)

# 2. Function for similarity search

def retrieve_info(query):
    similar_response = db.similarity_search(query, k=3)

    page_contents_array = [doc.page_content for doc in similar_response]

    return page_contents_array


# 3. Setup LLMChain & Prompts

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-16k-0613")

template = """
You are a world class nutritionist who specializes in creating meal plans,
and providing recipes for your patient. I will share a patients input for a custom meal plan with you.
Based on their diet preferences and goals or any other factors you know are important, 
you will create a custom meal-plan for them also include the ingredients, recipes, and calories for this plan.
You will follow ALL of the rules below:

1/ Response should be very clear and concise and should follow your patients preferences and requirements
as closely as possible

2/ You will be as accurate as possible and double check your meal-plan with the patients preferences
and requirements

3/ You will always provide the calories with each meal in the plan

Below is a message I received from a patient:
{message}

Here is the best possible meals based on their input:
{best_possible_meals}

Here are the calories for each the meals given:
{calorie_count}

Here are the ingredients in each meal you provide:
{ingredients}

Please write the best possible meal-plan that I should give to the patient:
"""

prompt = PromptTemplate(
    input_variables=["message", "best_possible_meals", "calorie_count", "ingredients"],
    template=template
)

chain = LLMChain(llm=llm, prompt=prompt)

# 4. Retrival augmented generation

def generate_response(message):
    best_possible_meals = retrieve_info(message)
    calorie_count = retrieve_info(message)
    ingredients = retrieve_info(message)
    response = chain.run(message=message, best_possible_meals=best_possible_meals, calorie_count=calorie_count,ingredients=ingredients)
    return response

def recipe_function(message):
    reply = generate_response(message)
    return reply