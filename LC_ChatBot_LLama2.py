from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

st.set_page_config(
    page_title="Langchain ChatBot",
    page_icon="🧊"
)


# Need to Disable when go for Deployment
load_dotenv()


# Need to Disable when go for Deployment
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


# Creating a PromptTemplate to structured input provided and behaviour of Model when providing response. 
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant named Mario. Please response to the user question"),
        ("user","Question:{question}")
    ]
)

st.title("Langchain ChatBot with LLAMA-2")
input_text = st.text_input("Search for any topic..")


# creating a Chain for sequencing of Prompts,llm,o/p parser
llm_llama2 = Ollama(model="llama2:7b")
output_parser = StrOutputParser()
chain = prompt|llm_llama2|output_parser


if input_text:
    st.write(chain.invoke({"question":input_text}))