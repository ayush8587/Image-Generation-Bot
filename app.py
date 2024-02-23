import streamlit as st
import requests
from PIL import Image
from io import BytesIO

API_URL = "https://flowise-website.onrender.com/api/v1/prediction/cc712a6d-6315-40c9-8767-c2387dcbf9d3"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

# Streamlit App
st.title("Image Generation Bot")

# Define a function to generate images based on user input
def generate_image(question):
    payload = {"question": question}
    response_json = query(payload)
    if "text" in response_json:
        image_url = response_json["text"]
        image_response = requests.get(image_url)
        img = Image.open(BytesIO(image_response.content))
        st.image(img, caption='Generated Image', use_column_width=True)
        download_button = st.download_button(
            label="Download Image",
            data=image_response.content,
            file_name="generated_image.png",
            mime="image/png"
        )
    else:
        st.error("Failed to generate image. Please try again.")

# User Input
user_input = st.text_input("Ask a question for image generation")

# Generate Image Button
if st.button("Generate Image"):
    if user_input.strip() != "":
        generate_image(user_input)
    else:
        st.warning("Please enter a question.")
