from dotenv import load_dotenv
load_dotenv()  # to load all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Loading gemini pro model
model = genai.GenerativeModel("gemini-pro-vision")

def get_response(prompt, image):
    if prompt!="":
        response=model.generate_content([prompt,image])
    else:
        response=model.generate_content(image)
    
    return response.text

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

st.set_page_config(page_title="Gemini LLM Demo")
st.markdown(custom_css, unsafe_allow_html=True)

# Centered header
st.title("GemCHAT")

# Create a custom container for input

st.text("How can I help you?")
input = st.text_input("", placeholder="Query about the image", key="input")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=500)

# Create a custom container for the button
button_container = st.container()

with button_container:
    submit = st.button("Ask GemCHAT")

# Display the response on top of the screen
if submit:
    output = get_response(input,image)
    st.subheader("Result")
    st.write(output)
