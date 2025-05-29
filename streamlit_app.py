import streamlit as st
import requests

st.set_page_config(page_title="Mental Health Chatbot", layout="centered")
st.title("Mental Health Support Chatbot")

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input("You:", "")

if st.button("Send") and user_input:
    # Display user input
    st.session_state.chat_history.append(("You", user_input))

    # Call FastAPI backend
    response = requests.post("http://127.0.0.1:8000/chat", json={"message": user_input})

    if response.status_code == 200:
        bot_reply = response.json().get("reply", "Sorry, I couldn't understand that.")
        st.session_state.chat_history.append(("Bot", bot_reply))
    else:
        st.session_state.chat_history.append(("Bot", "Error contacting backend."))

# Display chat
for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")
