import streamlit as st
from state.session import logout, set_page


def tela_inicial_view():
    # Sidebar
    with st.sidebar:

        nome = st.session_state.get("user_name", "Usuário")
        with st.expander(f"👤 Olá, {nome}"):
            # Menu do usuário
            if st.button("✏️ Editar perfil"):
                set_page("editar_usuario")

            if st.button("🚪 Logout"):
                logout()
                st.session_state.authenticated = False
                set_page("login")
                st.rerun()

        st.divider()

        # Menu Principal

        if st.button("📄 Currículos"):
            set_page("lista_curriculos")

    # Conteúdo principal
    st.title("Bem-vindo ao Job Evaluator!")

    st.write(
        """
        Aqui você poderá:
        - Criar e gerenciar seus currículos
        - Editar suas informações pessoais
        - Avaliar compatibilidade com vagas futuramente
        """
    )

    st.info("Selecione uma opção na barra lateral para começar.")
