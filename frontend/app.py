import streamlit as st
from views.Login import login_view
from views.Criar_Conta import criar_conta_view
from views.Redefinir_Senha import redefinir_senha_view
from views.Esqueci_Senha import esqueci_senha_view
from views.Usuario.Tela_Inicial import tela_inicial_view
from views.Usuario.Editar_Usuario import editar_usuario_view
from views.Curriculo.Listar_Curriculo import listar_curriculo_view
from views.Curriculo.Criar_Curriculo import criar_curriculo_view
from views.Curriculo.Editar_Curriculo import editar_curriculo_view
from state.session import is_logged, logout


st.set_page_config(page_title="Job Evaluator", layout="centered")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "page" not in st.session_state:
    st.session_state.page = "login"

query_params = st.query_params

if "page" in query_params:
    st.session_state.page = query_params["page"]

page = st.session_state.get("page", "login")

if page == "resetar_senha":
    redefinir_senha_view()

# Usuário não autenticado
if not st.session_state.authenticated:
    if st.session_state.page == "login":
        login_view()
    elif st.session_state.page == "criar_conta":
        criar_conta_view()
    elif st.session_state.page == "esqueci_senha":
        esqueci_senha_view()

# Usuário autenticado
else:
    if st.session_state.page == "tela_inicial":
        tela_inicial_view()
    elif st.session_state.page == "editar_usuario":
        editar_usuario_view()
    elif st.session_state.page == "lista_curriculos":
        listar_curriculo_view()
    elif st.session_state.page == "criar_curriculo":
        criar_curriculo_view()
    elif st.session_state.page == "editar_curriculo":
        editar_curriculo_view()
        