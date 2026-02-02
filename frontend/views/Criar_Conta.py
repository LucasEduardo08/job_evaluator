import streamlit as st
from services.auth_service import criar_conta
from state.session import set_page


def criar_conta_view():
    st.title("Criar Conta")

    # Preencher o formulário de criação de conta
    with st.form("criar_conta_form"):
        st.write("Preencha os dados abaixo para criar uma nova conta.")
        username = st.text_input("Nome Completo")
        nome = username
        email = st.text_input("Email")
        password = st.text_input("Senha", type="password")
        telefone = st.text_input("Telefone")
        endereco = st.text_input("Endereço")
        data_nascimento = st.date_input("Data de Nascimento")
        submitted = st.form_submit_button("Criar Conta")

    if submitted:
        success = criar_conta(username, password, email, nome, telefone, endereco, data_nascimento.isoformat())
        if success:
            st.success("Conta criada com sucesso! Volte para o login.")
        else:
            st.error("Erro ao criar conta. Tente novamente.")

    if st.button("Voltar para login"):
        set_page("login")
        st.rerun()
    