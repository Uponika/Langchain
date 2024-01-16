## QA Chatbot
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

import streamlit as st

## Function to load open ai models and get response

def get_openai_response(question):
    llm = OpenAI(openai_api_key = os.getenv('OPENAI_API_KEY'), model_name = 'gpt-3.5-turbo-instruct', temperature= 0.6)
    #llm = OpenAI(model_name = 'gpt-3.5-turbo-instruct', temperature= 0.6)
    response = llm(question)
    return response

## initialize streamlit app
    
st.set_page_config(page_title="Q/A demo")
st.header("Langchain Demo Chatbot")

# fetch the input data
input = st.text_input("Input: ", key="input")

response = get_openai_response(input)

submit = st.button("Ask the question")

## if submit is clicked

if submit:
    st.subheader("The Response is ")
    st.write(response)
