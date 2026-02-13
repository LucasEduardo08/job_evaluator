# Job Evaluator 🚀  
Sistema inteligente de avaliação e pontuação de currículos com uso de inteligência artificial.

Plataforma web desenvolvida em Django e Streamlit que permite o cadastro e gerenciamento de currículos e cadastro e gerenciamento de informações de usuário. No momento a parte de análise dos currículos ainda será implementada.

## 📌 Problema
Muitos candidatos enviam currículos sem saber se estão adequados para determinada vaga ou acham que o currículo não está bom. 

O Job Evaluator busca automatizar esse processo de avaliação utilizando ferramentas web e inteligência artificial para:

- Extrair informações do currículo
- Analisar compatibilidade com vagas
- Gerar pontuação explicável
- Sugerir melhorias
- Gerenciar currículos

## ⚙️ Funcionalidades
As funcionalidades atuais em funcionamento são:
### 🔐 Autenticação
- Cadastro e login com username
- Controle de sessão

### 📄 Gestão de Currículos
- Cadastro
- Edição
- Exclusão

### Gestão do Usuário
- Visualizar informação
- Editar informação

## 🏗 Arquitetura

O sistema foi desenvolvido seguindo separação de responsabilidades:
- Backend: Django
- Frontend: Streamlit
- Desenho do Banco de dados e diagramas: BRmodelo
- Banco de Dados: SQLite
- Deploy: Railway

## ▶️ Como executar
1. Clone o repositório
- git clone https://github.com/LucasEduardo08/job_evaluator
2. Crie o ambiente virtual
- python -m venv <venv>
3. Instale as dependências:
- pip install -r requirements.txt
4. Configure as variáveis de ambiente
5. Rode as migrações:
- python manage.py migrate
6. Execute o servidor:
- python manage.py runserver
7. Execute o frontend em outro terminal:
- streamlit run frontend/app.py

## 🚀 Fases do projeto

- [x] Base do sistema
- [ ] Upload e estrutura avançada
- [ ] Analisador de currículos
- [ ] Busca de Vagas de emprego

## 👨‍💻 Autor

Lucas Eduardo Pereira Teles  
Engenharia de Computação  
LinkedIn: www.linkedin.com/in/lucas-eduardo-pereira-teles-211093226
