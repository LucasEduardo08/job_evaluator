import streamlit as st
from services.auth_service import login
from state.session import set_page
from state.session import set_token, is_logged


def login_view():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Entrar"):
        token = login(username, password)
        if token:
            set_token(token)
            st.session_state.authenticated = True
            st.session_state.user_name = username
            set_page("tela_inicial")
            st.rerun()
        else:
            st.error("Credenciais inválidas")

    if st.button("Criar conta"):
        set_page("criar_conta")
        st.rerun()

    if st.button("Esqueci minha senha"):
        set_page("esqueci_senha")
        st.rerun()