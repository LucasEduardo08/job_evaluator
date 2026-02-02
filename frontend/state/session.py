import streamlit as st

def set_token(token):
    st.session_state["token"] = token

def get_token():
    return st.session_state.get("token")

def logout():
    if "token" in st.session_state:
        del st.session_state["token"]

    if "authenticated" in st.session_state:
        st.session_state.authenticated = False

    if "user_name" in st.session_state:
        del st.session_state["user_name"]

    st.session_state.page = "login"

def is_logged():
    return "token" in st.session_state

def set_page(page_name):
    st.session_state.page = page_name

def get_page():
    return st.session_state.get("page", "login")