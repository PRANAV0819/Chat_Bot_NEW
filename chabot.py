import streamlit as st
import google.generativeai as genai
import os

# Set API key properly
genai.configure(api_key=GEMINI_API_KEY)

# Check available models
models = genai.list_models()
available_models = [m.name for m in models]
print("Available Models:", available_models)

# Use the correct model if available
if "gemini-pro" in available_models:
    model = genai.GenerativeModel("gemini-pro")
else:
    st.error("gemini-pro model is not available for your API key. Check your Google AI Studio settings.")

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
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Get AI response
    if "gemini-pro" in available_models:
        response = model.generate_content(user_input)
        bot_response = response.text if response else "Sorry, I couldn't generate a response."
    else:
        bot_response = "Gemini-Pro model is not available."

    # Add AI message to history
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    
    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(bot_response)
