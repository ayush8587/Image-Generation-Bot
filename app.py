import streamlit as st
import requests

API_URL = "https://flowise-website.onrender.com/api/v1/prediction/cc712a6d-6315-40c9-8767-c2387dcbf9d3"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

def main():
    st.title("Image Generation Chatbot")

    question = st.text_input("Ask something:", "Hey, how are you?")

    if st.button("Generate Image"):
        override_config = {
            "template": "example",
            "promptValues": {"key": "val"},
            "replicateApiKey": "example",
            "model": "example",
        }
        payload = {
            "question": question,
            "overrideConfig": override_config
        }
        
        output = query(payload)
        
        # Assuming the response contains the URL of the generated image
        if "image_url" in output:
            st.image(output["image_url"], caption="Generated Image", use_column_width=True)
        else:
            st.error("Failed to generate image.")

if __name__ == "__main__":
    main()
