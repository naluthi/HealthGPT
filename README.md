# HealthGPT: Specialized Chatbots for Reliable Health Advice

![GitHub top language](https://img.shields.io/github/languages/top/naluthi/HealthGPT) 
[![Hugging Face](https://img.shields.io/badge/-Hugging%20Face-yellow?style=flat&logo=huggingface&logoColor=white)](https://huggingface.co/) 
[![LangChain](https://img.shields.io/badge/-LangChain-lightgrey?style=flat)](https://github.com/LangChain/langchain) 
[![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/) 

## Description

HealthGPT is an AI-powered chatbot designed with a focus on providing specialized health advice. During my summer internship, I was tasked with creating a chatbot, with the main goal of providing basic information to the user that was consistent and accurate. I created this chatbot before OpenAI's custom GPT features, which pushed me to learn and understand machine learning and large language models by leveraging the OpenAI API and HuggingFace's CSV data. The core idea was to train multiple 'specialty doctor' GPTs who could provide targeted advice based on health data similarities. This is also a 'first-take' at building this chatbot and was mainly used as a test case before building a Flask app and making the driver code more complex. 

I chose specific technologies to realize this vision:

- **HuggingFace:** For its extensive, free CSV data, easing integration.
- **OpenAI APIs:** Leading the field in AI with comprehensive guides and efficient character generation.
- **Langchain:** To seamlessly load CSV data and integrate OpenAI embeddings.
- **Pydantic:** For its speed and extensive data validation capabilities.
- **FastAPI:** Initially, I experimented with HTTP requests, but FastAPI's robustness eventually won me over for more complex web requests.

## Issues Addressed

- Improving the reliability of health advice given by chatbots.
- Creating a demo for user feedback, aiming to build a tool people would use and trust.

### Challenges and Learning
- Handling large CSV datasets and optimizing storage without incurring high costs was a significant hurdle.
- Implementing fastapi for specific chatbot functionalities required innovative solutions, leading to the development of a main function that categorizes chatbots and matches them with user queries.
- Transitioning from AWS lambda functions to Firebase hosting was necessary to overcome persistent errors and progress with the project.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [License](#license)
- [Contact](#contact)

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

## License

This project is available under the [MIT License](LICENSE). This allows other developers to use, modify, and distribute the project subject to the license terms.

# Contact 

[![Outlook](https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white)](nick@luthi.us) 
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nickluthi)
