from dotenv import load_dotenv
load_dotenv() ## to load all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## loading gemini pro model
 
model = genai.GenerativeModel("gemini-pro")

## function to get response from model

def get_response(query):
    response = model.generate_content(query)
    return response.text

st.set_page_config(page_title = "Gemini LLM Demo")

st.header("Gemini LLM Application")

input = st.text_input("Input :", key= "input")
submit = st.button("How Can I help you?")

if submit:
    output = get_response(input)
    st.subheader("Here you go! ")
    st.write(output)
