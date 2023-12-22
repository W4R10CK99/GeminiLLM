from dotenv import load_dotenv
load_dotenv()  # to load all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Loading gemini pro model
model = genai.GenerativeModel("gemini-pro")

# Function to get response from model
def get_response(query):
    response = model.generate_content(query)
    return response.text

# Custom CSS for gradient background and centering the header
custom_css = """
<style>
body {
    background: linear-gradient(to right, #ff7e5f, #feb47b) !important;
    color: white !important;
}
h1 {
    text-align: center;
}
</style>
"""

st.set_page_config(page_title="Gemini LLM Demo", page_icon=":gem:")
st.markdown(custom_css, unsafe_allow_html=True)

# Centered header
st.title("GemCHAT")

# Create a custom container for input
input_container = st.container()

with input_container:
    st.text("How can I help you?")
    input = st.text_input("", placeholder="Enter your problem here", key="input")

# Create a custom container for the button
button_container = st.container()

with button_container:
    submit = st.button("Send")

# Display the response on top of the screen
if submit:
    output = get_response(input)
    st.subheader("Here you go! ")
    st.write(output)
