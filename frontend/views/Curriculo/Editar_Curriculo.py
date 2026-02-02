import streamlit as st
from state.session import logout, set_page
from state.session import set_page, get_token
from services.curriculo import editar_curriculo, obter_curriculo


def editar_curriculo_view():
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
    st.title("✏️ Editar Currículo")

    token = get_token()
    curriculo_id = st.session_state.get("curriculo_id")

    if not token or not curriculo_id:
        st.error("Currículo não selecionado.")
        return

    # Carrega currículo apenas uma vez
    if "curriculo_carregado" not in st.session_state:
        curriculo = obter_curriculo(token, curriculo_id)

        if not curriculo:
            st.error("Erro ao carregar currículo.")
            return

        st.session_state["curriculo_carregado"] = True
        st.session_state["nome_curriculo"] = curriculo["nome_curriculo"]
        st.session_state["area_atuacao"] = curriculo["area_atuacao"]
        st.session_state["resumo_perfil"] = curriculo["resumo_perfil"]
        st.session_state["origem_curriculo"] = curriculo["origem_curriculo"]

        st.session_state["educacoes"] = curriculo["educacoes"]
        st.session_state["competencias"] = curriculo["competencias"]

    st.subheader("📄 Dados do currículo")

    nome_curriculo = st.text_input(
        "Nome do currículo",
        value=st.session_state["nome_curriculo"]
    )

    area_atuacao = st.text_input(
        "Área de atuação",
        value=st.session_state["area_atuacao"]
    )

    resumo_perfil = st.text_area(
        "Resumo do perfil",
        value=st.session_state["resumo_perfil"]
    )

    origem_curriculo = st.text_input(
        "Origem do currículo",
        value=st.session_state["origem_curriculo"]
    )

    st.subheader("🎓 Educações")

    for i, edu in enumerate(st.session_state["educacoes"]):

        with st.expander(f"Educação #{i+1}"):

            edu["instituicao"] = st.text_input(
                "Instituição",
                value=edu["instituicao"],
                key=f"inst_{i}"
            )

            edu["curso"] = st.text_input(
                "Curso",
                value=edu["curso"],
                key=f"curso_{i}"
            )

            edu["nivel_educacao"] = st.selectbox(
                "Nível",
                ["Ensino Médio", "Graduação", "Pós-graduação", "Mestrado", "Doutorado"],
                index=["Ensino Médio", "Graduação", "Pós-graduação", "Mestrado", "Doutorado"]
                    .index(edu["nivel_educacao"]),
                key=f"nivel_{i}"
            )

            edu["data_inicio"] = st.text_input(
                "Data início (YYYY-MM-DD)",
                value=edu["data_inicio"],
                key=f"ini_{i}"
            )

            edu["data_conclusao"] = st.text_input(
                "Data conclusão (YYYY-MM-DD)",
                value=edu["data_conclusao"],
                key=f"fim_{i}"
            )

            if st.button("🗑️ Remover educação", key=f"del_edu_{i}"):
                st.session_state["educacoes"].pop(i)
                st.rerun()

    st.subheader("➕ Adicionar nova educação")

    nova_inst = st.text_input("Instituição", key="new_inst")
    novo_curso = st.text_input("Curso", key="new_curso")
    novo_nivel = st.selectbox(
        "Nível",
        ["Ensino Médio", "Graduação", "Pós-graduação", "Mestrado", "Doutorado"],
        key="new_nivel"
    )
    nova_ini = st.text_input("Data início (YYYY-MM-DD)", key="new_ini")
    nova_fim = st.text_input("Data conclusão (YYYY-MM-DD)", key="new_fim")

    if st.button("Adicionar educação"):
        st.session_state["educacoes"].append({
            "instituicao": nova_inst,
            "curso": novo_curso,
            "nivel_educacao": novo_nivel,
            "data_inicio": nova_ini,
            "data_conclusao": nova_fim,
        })
        st.rerun()

    st.subheader("🧠 Competências")

    for i, comp in enumerate(st.session_state["competencias"]):

        with st.expander(comp["nome_competencia"]):

            comp["nome_competencia"] = st.text_input(
                "Nome",
                value=comp["nome_competencia"],
                key=f"nome_{i}"
            )

            comp["nivel_competencia"] = st.selectbox(
                "Nível",
                ["Básico", "Intermediário", "Avançado", "Especialista"],
                index=["Básico", "Intermediário", "Avançado", "Especialista"]
                    .index(comp["nivel_competencia"]),
                key=f"nivel_comp_{i}"
            )

            comp["descricao_competencia"] = st.text_area(
                "Descrição",
                value=comp["descricao_competencia"],
                key=f"desc_{i}"
            )

            if st.button("🗑️ Remover competência", key=f"del_comp_{i}"):
                st.session_state["competencias"].pop(i)
                st.rerun()

    st.subheader("➕ Adicionar nova competência")

    novo_nome = st.text_input("Nome da competência", key="new_comp_nome")
    novo_nivel = st.selectbox(
        "Nível",
        ["Básico", "Intermediário", "Avançado", "Especialista"],
        key="new_comp_nivel"
    )
    nova_desc = st.text_area("Descrição", key="new_comp_desc")

    if st.button("Adicionar competência"):
        st.session_state["competencias"].append({
            "nome_competencia": novo_nome,
            "nivel_competencia": novo_nivel,
            "descricao_competencia": nova_desc,
        })
        st.rerun()

    st.divider()

    if st.button("💾 Salvar currículo"):

        payload = {
            "nome_curriculo": nome_curriculo,
            "area_atuacao": area_atuacao,
            "resumo_perfil": resumo_perfil,
            "origem_curriculo": origem_curriculo,
            "educacoes": st.session_state["educacoes"],
            "competencias": st.session_state["competencias"],
        }

        sucesso = editar_curriculo(token, curriculo_id, payload)

        if sucesso:
            st.success("Currículo atualizado com sucesso!")
            st.session_state.pop("curriculo_carregado", None)
            set_page("lista_curriculos")
            st.rerun()
        else:
            st.error("Erro ao salvar currículo.")
            