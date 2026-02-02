import streamlit as st
from state.session import logout, set_page, get_token
from services.curriculo import criar_curriculo


def criar_curriculo_view():
    # =========================
    # SIDEBAR
    # =========================
    with st.sidebar:

        nome = st.session_state.get("user_name", "Usuário")

        with st.expander(f"👤 Olá, {nome}"):
            if st.button("✏️ Editar perfil"):
                set_page("editar_usuario")
                st.rerun()

            if st.button("🚪 Logout"):
                logout()
                st.session_state.authenticated = False
                set_page("login")
                st.rerun()

        st.divider()

        if st.button("📄 Currículos"):
            set_page("lista_curriculos")
            st.rerun()

    # =========================
    # ESTADOS INICIAIS
    # =========================
    if "competencias" not in st.session_state:
        st.session_state.competencias = []

    if "educacoes" not in st.session_state:
        st.session_state.educacoes = []

    # =========================
    # CONTEÚDO PRINCIPAL
    # =========================
    st.title("➕ Criar Currículo")

    # =========================
    # BLOCO: COMPETÊNCIAS (fora do form)
    # =========================
    st.subheader("Competências")

    col1, col2, col3 = st.columns(3)

    with col1:
        nome_comp = st.text_input("Nome da competência")

    with col2:
        nivel_comp = st.selectbox("Nível", ["Básico", "Intermediário", "Avançado", "Especialista"])

    with col3:
        desc_comp = st.text_input("Descrição curta")

    if st.button("➕ Adicionar competência"):
        if nome_comp:
            st.session_state.competencias.append({
                "nome_competencia": nome_comp,
                "nivel_competencia": nivel_comp,
                "descricao_competencia": desc_comp,
            })
            st.rerun()
        else:
            st.warning("Informe o nome da competência.")

    # Mostrar competências adicionadas
    for i, comp in enumerate(st.session_state.competencias):
        st.info(f"{i+1}. {comp['nome_competencia']} ({comp['nivel_competencia']})")

    st.divider()

    # =========================
    # BLOCO: EDUCAÇÃO (fora do form)
    # =========================
    st.subheader("Educação")

    col1, col2 = st.columns(2)

    with col1:
        instituicao = st.text_input("Instituição")

    with col2:
        curso = st.text_input("Curso")

    nivel_edu = st.selectbox(
        "Nível de educação",
        ["Ensino Médio", "Graduação", "Pós-graduação", "Mestrado", "Doutorado"]
    )

    col3, col4 = st.columns(2)

    with col3:
        data_inicio = st.date_input("Data de início")

    with col4:
        data_conclusao = st.date_input("Data de conclusão")

    if st.button("➕ Adicionar formação"):
        if instituicao and curso:
            st.session_state.educacoes.append({
                "instituicao": instituicao,
                "curso": curso,
                "nivel_educacao": nivel_edu,
                "data_inicio": data_inicio.isoformat(),
                "data_conclusao": data_conclusao.isoformat(),
            })
            st.rerun()
        else:
            st.warning("Informe instituição e curso.")

    # Mostrar educações adicionadas
    for i, edu in enumerate(st.session_state.educacoes):
        st.info(f"{i+1}. {edu['curso']} - {edu['instituicao']}")

    st.divider()

    # =========================
    # FORMULÁRIO FINAL (só dados principais + submit)
    # =========================
    with st.form("form_criar_curriculo"):

        nome_curriculo = st.text_input("Nome do currículo")
        area_atuacao = st.text_input("Área de atuação")
        resumo_perfil = st.text_area("Resumo do perfil")
        origem_curriculo = st.text_input("Origem do currículo")

        submit = st.form_submit_button("💾 Criar currículo")

    # =========================
    # ENVIO PARA API
    # =========================
    if submit:

        if not nome_curriculo:
            st.error("Nome do currículo é obrigatório.")
            return

        dados = {
            "nome_curriculo": nome_curriculo,
            "area_atuacao": area_atuacao,
            "resumo_perfil": resumo_perfil,
            "origem_curriculo": origem_curriculo,
            "competencias": st.session_state.competencias,
            "educacoes": st.session_state.educacoes,
        }

        sucesso = criar_curriculo(get_token(), dados)

        if sucesso:
            st.success("Currículo criado com sucesso!")

            # Limpa estados
            st.session_state.competencias = []
            st.session_state.educacoes = []

            set_page("lista_curriculos")
            st.rerun()
        else:
            st.error("Erro ao criar currículo. Verifique os dados.")
