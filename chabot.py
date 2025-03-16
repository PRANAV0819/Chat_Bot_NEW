import streamlit as st
import google.generativeai as genai

# Set your Gemini API Key here
import os
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# Configure Google Gemini API
genai.configure(api_key=GEMINI_API_KEY)
models = genai.list_models()

for m in models:
    print(m.name)

# Streamlit UI
st.title("💬 AI Chatbot with Google Gemini")
st.markdown("### Powered by Google's Gemini Model")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your message here...")
if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Get AI response
    response = model.generate_content(user_input)
    bot_response = response.text if response else "Sorry, I couldn't generate a response."
    
    # Add AI message to history
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    
    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(bot_response)
