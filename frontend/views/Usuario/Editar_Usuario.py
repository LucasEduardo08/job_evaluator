import streamlit as st
from state.session import set_page, get_token
from services.usuario import atualizar_usuario, obter_usuario


def editar_usuario_view():
    st.title("Perfil do Usuário")

    if "editando_usuario" not in st.session_state:
        st.session_state.editando_usuario = False

    token = get_token()
    if not token:
        st.error("Token de usuário não encontrado.")
        return

    usuario = obter_usuario(token)
    if not usuario:
        st.error("Erro ao carregar os dados do usuário.")
        return

    # Modo Visualização
    if not st.session_state.editando_usuario:
        col1, col2 = st.columns([5, 1])

        with col1:
            if st.button("⬅️ Voltar"):
                set_page("tela_inicial")
                st.rerun()

        with col2:
            if st.button("✏️", help="Editar dados"):
                st.session_state.editando_usuario = True
                st.rerun()

        st.text_input("Nome", value=usuario.get("nome", ""), disabled=True)
        st.text_input("Email", value=usuario.get("email", ""), disabled=True)
        st.text_input("Telefone", value=usuario.get("telefone", ""), disabled=True)
        st.text_input("Endereço", value=usuario.get("endereco", ""), disabled=True)
        st.text_input(
            "Data de nascimento",
            value=str(usuario.get("data_nascimento", "")),
            disabled=True,
        )

        return

    # Modo Edição
    st.subheader("Editar informações")

    with st.form("form_editar_usuario"):
        nome = st.text_input("Nome", value=usuario.get("nome", ""))
        email = st.text_input("Email", value=usuario.get("email", ""))
        telefone = st.text_input("Telefone", value=usuario.get("telefone", ""))
        endereco = st.text_input("Endereço", value=usuario.get("endereco", ""))
        data_nascimento = st.date_input(
            "Data de nascimento",
            value=None if not usuario.get("data_nascimento") else usuario.get("data_nascimento"),
            format="YYYY-MM-DD",
        )

        col1, col2 = st.columns(2)

        with col1:
            salvar = st.form_submit_button("💾 Salvar")

        with col2:
            cancelar = st.form_submit_button("❌ Cancelar")

    if salvar:
        sucesso = atualizar_usuario(
            token,
            nome,
            email,
            telefone,
            endereco,
            data_nascimento,
        )

        if sucesso:
            st.success("Dados atualizados com sucesso!")
            st.session_state.editando_usuario = False
            st.rerun()
        else:
            st.error("Erro ao atualizar os dados.")

    if cancelar:
        st.session_state.editando_usuario = False
        st.rerun()
