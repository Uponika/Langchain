## Conversational Q&A Chatbot

import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

## Streamlit UI

st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey!! Let's chat")

load_dotenv()

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content =  "You are a comedian AI assistant!")
    ]

chat = ChatOpenAI(openai_api_key = os.getenv('OPENAI_API_KEY'), temperature = 0.5)

def get_chatmodel_response(question):

    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content


# fetch the input data
input = st.text_input("Input: ", key="input")

response = get_chatmodel_response(input)

submit = st.button("Ask the question")

## if submit is clicked

if submit:
    st.subheader("The Response is ")
    st.write(response)