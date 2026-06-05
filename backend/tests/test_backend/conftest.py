import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User
from polls.models import Usuario


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def data():
    return {
        "username": "Lindinha01",
        "email": "lindinha@gmail.com",
        "password": "12345678",
        "nome": "Lindinha",
        "telefone": "(92) 99999-9999",
        "endereco": "Rua X",
        "data_nascimento": "2002-08-10"
    }

@pytest.fixture
def curriculo_data():
    return {
        "nome_curriculo": "Backend Python",
        "area_atuacao": "Desenvolvedor Backend",
        "resumo_perfil": "Desenvolvedor Python com foco em APIs",
        "origem_curriculo": "LinkedIn",

        "educacoes": [
            {
                "instituicao": "UEA",
                "curso": "Engenharia da Computação",
                "nivel_educacao": "Graduação",
                "data_inicio": "2021-01-01",
                "data_conclusao": "2025-12-01"
            }
        ],

        "competencias": [
            {
                "nome_competencia": "Python",
                "nivel_competencia": "Avançado",
                "descricao_competencia": "APIs, Django, FastAPI"
            },
            {
                "nome_competencia": "Machine Learning",
                "nivel_competencia": "Intermediário",
                "descricao_competencia": "PyTorch, NLP"
            }
        ]
    }

@pytest.fixture
def post_criar_usuario(api_client):
    """
    Factory fixture para criar usuários.
    """

    def _post_criar_usuario(payload):
        url = reverse("criar_usuario")
        return api_client.post(url, payload, format="json")

    return _post_criar_usuario

@pytest.fixture
def usuario_criado(data):
    user = User.objects.create_user(
        username=data["username"],
        email=data["email"],
        password=data["password"]
    )

    usuario = Usuario.objects.create(
        user=user,
        nome=data["nome"],
        telefone=data["telefone"],
        endereco=data["endereco"],
        data_nascimento=data["data_nascimento"]
    )

    return user

@pytest.fixture
def api_client_autenticado(api_client, usuario_criado):
    """
    Autentica o usuário automaticamente evitando gerar token de forma manual
    """
    
    api_client.force_authenticate(user=usuario_criado)

    return api_client

@pytest.fixture
def get_usuario(api_client_autenticado):
    """
    Factory para obter usuário autenticado
    """

    def _get_usuario():
        url = reverse("usuario_me")
        return api_client_autenticado.get(url)

    return _get_usuario

@pytest.fixture
def put_usuario(api_client_autenticado):
    """
    Factory para editar usuário autenticado
    """

    def _put_usuario(payload):
        url = reverse("editar_usuario")
        return api_client_autenticado.put(
            url, 
            payload, 
            format="json")

    return _put_usuario

@pytest.fixture
def delete_usuario(api_client_autenticado):

    def _delete_usuario():
        url = reverse("deletar_usuario")
        return api_client_autenticado.delete(url)

    return _delete_usuario
