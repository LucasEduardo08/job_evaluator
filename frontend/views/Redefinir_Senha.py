import streamlit as st
import requests
from config import API_URL
from state.session import set_page


def redefinir_senha_view(request):
    query_params = st.query_params
    token = query_params.get("token")

    st.title("🔐 Redefinir senha")

    if not token:
        st.error("Token inválido")
        return

    nova_senha = st.text_input("Nova senha", type="password")

    if st.button("Salvar nova senha"):
        if redefinir_senha(token, nova_senha):
            st.success("Senha alterada com sucesso!")
            set_page("login")
            st.rerun()
        else:
            st.error("Token inválido ou expirado")
