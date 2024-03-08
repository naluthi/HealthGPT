# HealthGPT

![GitHub top language](https://img.shields.io/github/languages/top/naluthi/HealthGPT) 
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/naluthi/HealthGPT) 
[![LangChain](https://img.shields.io/badge/-LangChain-lightgrey?style=flat)](https://github.com/LangChain/langchain) 
[![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/) 

## Description

HealthGPT is an AI-powered chatbot designed with a focus on providing specialized health advice. During my summer internship, I was tasked with creating a chatbot, with the main goal of providing basic information to the user that was consistent and accurate. I created this chatbot before OpenAI's custom GPT features, which pushed me to learn and understand machine learning and large language models by leveraging the OpenAI API and HuggingFace's CSV data. The core idea was to train multiple 'specialty doctor' GPTs who could provide targeted advice based on health data similarities. This is also a 'first take' at building this chatbot and was mainly used as a test case before building a Flask app and making the driver code more complex. 

## Table of Contents
- [Description](#description)
- [Tools](#tools)
- [Solutions](#solutions)
- [Challenges](#challenges)
- [Features](#features)
- [Installation](#installation)
- [Contact](#contact)
  
## Tools
- **Langchain:** To seamlessly load CSV data and integrate OpenAI embeddings.
- **FAISS:** Used for efficient similarity search among documents loaded from CSV files. This is part of the LangChain integration and is useful for large datasets.
- **OpenAI APIs:** Leading the field in AI with comprehensive guides and efficient character generation.
- **FastAPI:** Initially, I experimented with HTTP requests, but FastAPI's robustness eventually won me over for more complex web requests.
- **HuggingFace:** For its extensive, free CSV data, easing integration.
- **Pydantic:** For its speed and extensive data validation capabilities.
  
## Solutions

- Improving the reliability of health advice given by chatbots.
- Creating a demo for user feedback, aiming to build a tool people would use and trust.

### Challenges

- Handling large CSV datasets and optimizing storage without incurring high costs was a significant hurdle.
- Implementing fastapi for specific chatbot functionalities required innovative solutions, leading to the development of a main function that categorizes chatbots and matches them with user queries.
- Transitioning from AWS lambda functions to Firebase hosting was necessary to overcome persistent errors and progress with the project.

## Features

- `main.py`: The heart of HealthGPT, orchestrating the chatbot's operations.
- `my_tools.py`: Contains utility functions and helpers.
- `coach.py`: Integrates lifestyle and wellness coaching.
- `doctor-data.py`: Manages health data for personalized advice.
- `doctor.py`: Simulates a general practitioner's advice.
- `find_dr.py`: Helps locate specialists based on user needs.
- `fitness.py`: Offers tailored fitness guidance.
- `mealplan.py`: Generates personalized meal plans.
- `recipes.py`: Provides healthy recipes.
- `research.py`: Gives access to health research and findings.
- `treatments.py`: Advises on treatments for various conditions.

## Installation

To get HealthGPT up and running, follow these steps:

1. Clone the repository:
```md
git clone https://github.com/naluthi/HealthGPT.git
```

2. Install the required dependencies:
```md
pip install -r requirements.txt
```

# Contact 

[![Outlook](https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white)](nick@luthi.us) 
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nickluthi)
