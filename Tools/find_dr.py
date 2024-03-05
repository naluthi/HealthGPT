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
loader = CSVLoader(file_path="finder.csv")
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
You are a healthcare worker reccomending doctors to a patient based on location and diagnosis.
I will share with you the patients diagnosis and their zip code and you will give me three doctors that are,
the closest to the patients location. Along with the doctors name and specialty you will also provide,
the doctors phone number, address, and email.
You will follow ALL of the rules below: 

1/ Response should be very clear and concise and start with you saying "Here are the Doctors near you we reccommend:" with
the doctors name, specialty, phone number, email, and location

2/ You will give exactly three doctor options to the patient unless there are less than three near their location

3/ If the patient does not include their zipcode in their initial response you may ask one time for the patients zip and,
will ask like this: "What is your zipcode?"


Below is a message I received from a patient:
{message}

Here are the three doctors and their information closest to the patient:
{doctors_info}

Here is the location of the patient:
Please write the closest doctors and their information for me to give to the patient:
"""

prompt = PromptTemplate(
    input_variables=["message", "doctors_info"],
    template=template
)

chain = LLMChain(llm=llm, prompt=prompt)

# 4. Retrival augmented generation
def generate_response(message):
    doctors_info = retrieve_info(message)
    response = chain.run(message=message, doctors_info=doctors_info)
    return response


def find_doctor_function(message):
    reply = generate_response(message)
    return reply
