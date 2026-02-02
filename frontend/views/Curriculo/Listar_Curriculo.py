import streamlit as st
from state.session import logout, set_page
from state.session import set_page, get_token
from services.curriculo import obter_curriculos
from components.confirmacao_delete import confirmar_exclusao_curriculo


def listar_curriculo_view():
    # Sidebar
    with st.sidebar:

        nome = st.session_state.get("user_name", "Usuário")
        with st.expander(f"👤 Olá, {nome}"):
            # Menu do usuário
            if st.button("✏️ Editar perfil"):
                set_page("editar_usuario")
                st.rerun()

            if st.button("🚪 Logout"):
                logout()
                st.session_state.authenticated = False
                set_page("login")
                st.rerun()

        st.divider()

        # Menu Principal
        if st.button("🏠 Início"):
            set_page("tela_inicial")
            st.rerun()

        if st.button("📄 Currículos"):
            set_page("lista_curriculos")

    # Conteúdo Principal
    st.title("📄 Meus Currículos")

    token = get_token()
    if not token:
        st.error("Token de usuário não encontrado.")
        return
    
    curriculos = obter_curriculos(token)

    col1, col2 = st.columns([3, 1])

    with col2:
        if st.button("➕ Criar currículo"):
            set_page("criar_curriculo")
            st.rerun()

    st.divider()

    if not curriculos:
        st.info("Você ainda não possui nenhum currículo cadastrado.")
        return

    # Tabela de currículos
    for curriculo in curriculos:
        col1, col2, col3, col4 = st.columns([4, 3, 1, 1])

        with col1:
            st.write(f"**{curriculo.get('nome_curriculo')}**")

        with col2:
            st.write(curriculo.get("area_atuacao", "-"))

        with col3:
            if st.button("✏️", key=f"editar_{curriculo['id']}", help="Editar currículo"):
                st.session_state.curriculo_id = curriculo["id"]
                set_page("editar_curriculo")
                st.rerun()

        with col4:
            if st.button("🗑️", key=f"deletar_{curriculo['id']}", help="Deletar currículo"):
                st.session_state["confirmar_exclusao"] = True
                st.session_state["curriculo_id"] = curriculo["id"]
                st.rerun()

        st.divider()
        confirmar_exclusao_curriculo()
