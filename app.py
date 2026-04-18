import streamlit as st
import google.generativeai as genai

# Sahifa sozlamasi
st.set_page_config(page_title="AqlVoy Yordamchi", page_icon="🎓")
st.title("AqlVoy Yordamchi 🎓")

# API kaliti
api_key = "AIzaSyAregfoifufu0owMdi05ysRg2IXaaHpEk4"
genai.configure(api_key=api_key)

# Modelni tanlash
model = genai.GenerativeModel('gemini-1.5-flash')

# Chat tarixini boshqarish
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Chat oynalarini ko'rsatish
for message in st.session_state.chat.history:
    with st.chat_message("user" if message.role == "user" else "assistant"):
        st.markdown(message.parts[0].text)

# Foydalanuvchi yozadigan joy
if user_input := st.chat_input("Savolingizni yozing..."):
    # Foydalanuvchi xabarini ekranga chiqarish
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Javob olish
    try:
        response = st.session_state.chat.send_message(user_input)
        with st.chat_message("assistant"):
            st.markdown(response.text)
    except Exception as e:
        st.error(f"Xatolik yuz berdi: {e}")
