import streamlit as st
import google.generativeai as genai

# Set API key
API_KEY = "your_actual_api_key_here"  # Replace with your API key
genai.configure(api_key=API_KEY)

# Check available models
models = genai.list_models()
available_models = [m.name for m in models]

# Use the correct model
if "gemini-1.5-pro" in available_models:
    model = genai.GenerativeModel("gemini-1.5-pro")  # ✅ Use an available model
elif "gemini-1.5-flash" in available_models:
    model = genai.GenerativeModel("gemini-1.5-flash")  # ✅ Faster option
else:
    st.error("❌ No suitable Gemini model found. Check Google AI Studio.")
    model = None

# Streamlit UI
st.title("💬 AI Chatbot with Google Gemini")

if model:
    user_input = st.text_input("Type your message here:")
    if user_input:
        response = model.generate_content(user_input)
        st.write(response.text if response else "⚠️ No response from AI.")
else:
    st.error("AI Model is not available. Check API settings.")
