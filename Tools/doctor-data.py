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
loader = CSVLoader(file_path="Data/diagnose.csv")
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
You are a world class medical doctor who specializes in both, 
western medicine and naturalpathic medicine. I will share a patients symptoms with you, 
and you will give me three to four of the best possible diagnosis' for the patient based on past best practices,
as well as the symptoms related to all three to four diagnosis' you respond with.
and you will follow ALL of the rules below:  

1/ Response should be very clear and concise and start with you saying "Possible Diagnosis" with
the diagnosis (1-3) that you are given followed by your best educated guess

2/ You will be as accurate as possible and double check your diagnosis

Below is a message I received from a patient:
{message}

Here is the best possible diagnosis given your patients symptoms:
{best_possible_diagnosis}
{best_possible_diagnosis}
{best_possible_diagnosis}

Here is the symptoms related to the diagnosis:
{related_symptoms}
{related_symptoms}
{related_symptoms}

Please write the best diagnosis that I should tell the patient:
"""

prompt = PromptTemplate(
    input_variables=["message", "best_possible_diagnosis", "related_symptoms"],
    template=template
)

chain = LLMChain(llm=llm, prompt=prompt)

# 4. Retrival augmented generation

def generate_response(message):
    best_possible_diagnosis = retrieve_info(message)
    related_symptoms = retrieve_info(message)
    response = chain.run(message=message, best_possible_diagnosis=best_possible_diagnosis, related_symptoms=related_symptoms)
    return response

message = input("List your symptoms: ")
response = generate_response(message)

print("\n" + response)