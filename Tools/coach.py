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
loader = CSVLoader(file_path="fitness_data.csv")
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
You are a world class personal trainer and kinesiologist who specializes in giving fitness tips and advice, 
and creating plans to help people achieve their fitness goals. I will share a clients questions and/or goals with you, 
and you will give me the best possible response to the clients message,
and you will follow ALL of the rules below:  

1/ Response should be your expert opinion and be very clear and concise 

2/ You will address all of the goals and preferences of the client

Below is a message I received from a client:
{message}

Here is the your expert opinion
{expert_opinion}


Please write the best diagnosis that I should tell the patient:
"""

prompt = PromptTemplate(
    input_variables=["message", "expert_opinion"],
    template=template
)

chain = LLMChain(llm=llm, prompt=prompt)

# 4. Retrival augmented generation
def generate_response(message):
    expert_opinion = retrieve_info(message)
    response = chain.run(message=message, expert_opinion=expert_opinion)
    return response

def fitness_coach(message):
    reply = generate_response(message)
    return reply
