import streamlit as st

st.title("Chat Interface Example")

# User message
with st.chat_message("user"):
    st.write("Hello 👋")

# Assistant reply
with st.chat_message("assistant"):
    st.write("Hi there! How can I help you today? 🤖")