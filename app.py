import streamlit as st
import google.generativeai as genai

# Page configuration
st.set_page_config(page_title="AqlVoy Yordamchi", page_icon="🎓")

st.title("AqlVoy Yordamchi 🎓")
st.write("Salom! Men AqlVoy, senga o'qishda yordam berishga tayyorman.")

# API Configuration - Make sure to keep this safe in a real project
api_key = "AIzaSyAregfoifufu0owMdi05ysRg2IXaaHpEk4"
genai.configure(api_key=api_key)

# Initialize the model
model = genai.GenerativeModel('gemini-pro')

# Initialize chat session
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Display chat history
for message in st.session_state.chat.history:
    with st.chat_message("user" if message.role == "user" else "assistant"):
        st.markdown(message.parts[0].text)

# Chat input
if user_input := st.chat_input("Savolingizni yozing..."):
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Generate response
    response = st.session_state.chat.send_message(user_input)
    
    # Display assistant message
    with st.chat_message("assistant"):
        st.markdown(response.text)
