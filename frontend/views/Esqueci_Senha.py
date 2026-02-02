import streamlit as st
import requests
from config import API_URL


def esqueci_senha_view():
    st.title("🔑 Esqueci minha senha")

    email = st.text_input("Digite seu email")

    if st.button("Enviar"):
        res = requests.post(
            f"{API_URL}/auth/reset-senha/",
            json={"email": email}
        )

        if res.status_code == 200:
            st.success("Se o email existir, você receberá instruções.")

    if st.button("Voltar ao login"):
        st.session_state.page = "login"
        st.rerun()
