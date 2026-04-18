import streamlit as st
import google.generativeai as genai

# 1. Sahifa sozlamalari
st.set_page_config(page_title="AqlVoy Yordamchi", page_icon="🎓")
st.title("AqlVoy Yordamchi 🎓")

# 2. API kaliti va modelni sozlash
api_key = "AIzaSyAregfoifufu0owMdi05ysRg2IXaaHpEk4"
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. Chat tarixini saqlash
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# 4. Chat interfeysi
for message in st.session_state.chat.history:
    with st.chat_message("user" if message.role == "user" else "assistant"):
        st.markdown(message.parts[0].text)

if user_input := st.chat_input("Savolingizni yozing..."):
    with st.chat_message("user"):
        st.markdown(user_input)
    
    try:
        response = st.session_state.chat.send_message(user_input)
        with st.chat_message("assistant"):
            st.markdown(response.text)
    except Exception as e:
        st.error(f"Xatolik: {e}")
