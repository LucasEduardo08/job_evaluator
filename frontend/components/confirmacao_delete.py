import streamlit as st
from state.session import set_page, get_token
from services.curriculo import deletar_curriculo


def confirmar_exclusao_curriculo():
    if not st.session_state.get("confirmar_exclusao"):
        return

    st.warning("⚠️ Tem certeza que deseja apagar este currículo? Essa ação não pode ser desfeita.")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Sim, apagar"):
            token = get_token()
            curriculo_id = st.session_state.get("curriculo_id")

            if deletar_curriculo(token, curriculo_id):
                st.success("Currículo apagado com sucesso!")
                st.session_state.pop("confirmar_exclusao", None)
                st.session_state.pop("curriculo_id", None)
                set_page("lista_curriculos")
                st.rerun()
            else:
                st.error("Erro ao apagar currículo.")

    with col2:
        if st.button("❌ Cancelar"):
            st.session_state["confirmar_exclusao"] = False
            st.rerun()
