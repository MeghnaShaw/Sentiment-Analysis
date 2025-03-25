import streamlit as st
from transformers import pipeline

classifier = pipeline("text-classification", framework="pt")

# Streamlit UI
st.title("Sentiment Analysis App")
st.write("Enter text to analyze sentiment.")

# User input
user_input = st.text_area("Enter your text here:")

if st.button("Analyze Sentiment"):
    if user_input:
        result = classifier(user_input)[0]
        label = result["label"]
        score = result["score"]
        
        # Display result
        st.write(f"*Sentiment:* {label}")
        st.write(f"*Confidence Score:* {score:.4f}")
    else:
        st.write("Please enter some text.")