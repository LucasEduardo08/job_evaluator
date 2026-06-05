import pytest
from http import HTTPStatus
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_cadastrar_usuario_sucesso(post_criar_usuario, data):

    response = post_criar_usuario(data)

    assert response.status_code == HTTPStatus.CREATED
    assert response.data["message"] == "User created successfully"

    assert User.objects.filter(
        username=data["username"]
    ).exists(), "User not exits"


@pytest.mark.django_db
def test_cadastrar_usuario_email_existente(post_criar_usuario, data):

    post_criar_usuario(data)

    # Tenta criar outro usuário com mesmo email
    payload_conflito = data.copy()
    payload_conflito["username"] = "outro_usuario"

    response = post_criar_usuario(payload_conflito)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.data["error"] == "Email already exists"


@pytest.mark.django_db
def test_cadastrar_usuario_username_existente(post_criar_usuario, data):

    post_criar_usuario(data)

    # Mesmo username, email diferente
    payload_conflito = data.copy()
    payload_conflito["email"] = "novoemail@gmail.com"

    response = post_criar_usuario(payload_conflito)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.data["error"] == "Username already exists"


@pytest.mark.django_db
def test_cadastrar_usuario_email_invalido(post_criar_usuario, data):

    payload = data.copy()
    payload["email"] = "email_invalido"

    response = post_criar_usuario(payload)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.data["error"] == "Invalid email address"


@pytest.mark.django_db
def test_cadastrar_usuario_senha_vazia(post_criar_usuario, data):

    payload = data.copy()
    payload["password"] = ""

    response = post_criar_usuario(payload)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.data["error"] == "Some data is missing"


@pytest.mark.django_db
def test_cadastrar_usuario_senha_invalida(post_criar_usuario, data):

    payload = data.copy()
    payload["password"] = "1234"

    response = post_criar_usuario(payload)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.data["error"] == "Password must have at least 8 characters"


@pytest.mark.django_db
def test_cadastrar_usuario_email_vazio(post_criar_usuario, data):

    payload = data.copy()
    payload["email"] = ""

    response = post_criar_usuario(payload)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.data["error"] == "Some data is missing"


@pytest.mark.django_db
def test_cadastrar_usuario_email_incompleto(post_criar_usuario, data):

    payload = data.copy()
    payload["email"] = "lindinha01@.com"

    response = post_criar_usuario(payload)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.data["error"] == "Invalid email address"


@pytest.mark.django_db
def test_cadastrar_usuario_nome_vazio(post_criar_usuario, data):

    payload = data.copy()
    payload["nome"] = ""

    response = post_criar_usuario(payload)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.data["error"] == "Some data is missing"


@pytest.mark.django_db
def test_cadastrar_usuario_nome_invalido(post_criar_usuario, data):

    payload = data.copy()
    payload["nome"] = "123"

    response = post_criar_usuario(payload)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.data["error"] == "Invalid name"


@pytest.mark.django_db
def test_cadastrar_usuario_telefone_vazio(post_criar_usuario, data):

    payload = data.copy()
    payload["telefone"] = ""

    response = post_criar_usuario(payload)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.data["error"] == "Some data is missing"


@pytest.mark.django_db
def test_cadastrar_usuario_telefone_invalido(post_criar_usuario, data):

    payload = data.copy()
    payload["telefone"] = "ade"

    response = post_criar_usuario(payload)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.data["error"] == "Invalid phone number"


@pytest.mark.django_db
def test_cadastrar_usuario_telefone_incompleto(post_criar_usuario, data):

    payload = data.copy()
    payload["telefone"] = "(92) "

    response = post_criar_usuario(payload)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.data["error"] == "Invalid phone number"


@pytest.mark.django_db
def test_cadastrar_usuario_endereco_vazio(post_criar_usuario, data):

    payload = data.copy()
    payload["endereco"] = ""

    response = post_criar_usuario(payload)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.data["error"] == "Some data is missing"
    

@pytest.mark.django_db
def test_cadastrar_usuario_data_nascimento_vazio(post_criar_usuario, data):

    payload = data.copy()
    payload["data_nascimento"] = ""

    response = post_criar_usuario(payload)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.data["error"] == "Some data is missing"


@pytest.mark.django_db
def test_cadastrar_usuario_data_nascimento_inválido(post_criar_usuario, data):

    payload = data.copy()
    payload["data_nascimento"] = "aop"

    response = post_criar_usuario(payload)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.data["error"] == "Invalid date"


@pytest.mark.django_db
def test_cadastrar_usuario_data_nascimento_incompleto(post_criar_usuario, data):

    payload = data.copy()
    payload["data_nascimento"] = "2019-"

    response = post_criar_usuario(payload)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.data["error"] == "Invalid date"
