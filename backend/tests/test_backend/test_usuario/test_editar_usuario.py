import pytest
from http import HTTPStatus
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_obter_usuario_sucesso(get_usuario, data):

    response = get_usuario()

    assert response.status_code == HTTPStatus.OK
    assert response.data["usuario"]["username"] == data["username"]
    assert response.data["usuario"]["email"] == data["email"]


@pytest.mark.django_db
def test_editar_usuario_nome(put_usuario, usuario_criado):
    
    payload = {
        "nome": "Novo Nome"
    }

    reponse = put_usuario(payload)
    usuario_criado.refresh_from_db()  # Atualiza o banco
    assert reponse.status_code == HTTPStatus.OK
    assert usuario_criado.usuario.nome == payload["nome"]


@pytest.mark.django_db
def test_editar_usuario_nome_invalido(put_usuario, usuario_criado):
    
    payload = {
        "nome": "Nome123"
    }

    reponse = put_usuario(payload)
    usuario_criado.refresh_from_db()  # Atualiza o banco
    assert reponse.status_code == HTTPStatus.BAD_REQUEST
    assert reponse.data["error"] == "Invalid name"


@pytest.mark.django_db
def test_editar_usuario_email_sucesso(put_usuario, usuario_criado):
    
    payload = {
        "email": "NovoEmail@gmail.com"
    }

    reponse = put_usuario(payload)
    usuario_criado.refresh_from_db()  # Atualiza o banco
    assert reponse.status_code == HTTPStatus.OK
    assert usuario_criado.usuario.email == payload["email"]


@pytest.mark.django_db
def test_editar_usuario_email_invalido(patch_usuario, usuario_criado):
    
    payload = {
        "email": "NovoEmail"
    }

    reponse = patch_usuario(payload)
    usuario_criado.refresh_from_db()  # Atualiza o banco
    assert reponse.status_code == HTTPStatus.BAD_REQUEST
    assert reponse.data["error"] == "Dados inválidos"


@pytest.mark.django_db
def test_editar_usuario_email_vazio(patch_usuario, usuario_criado):
    
    payload = {
        "email": ""
    }

    reponse = patch_usuario(payload)
    usuario_criado.refresh_from_db()  # Atualiza o banco
    assert reponse.status_code == HTTPStatus.BAD_REQUEST
    assert reponse.data["error"] == "Campo vazio"


@pytest.mark.django_db
def test_editar_usuario_nome_sucesso(patch_usuario, usuario_criado):
    
    payload = {
        "nome": "Novo Nome"
    }

    reponse = patch_usuario(payload)
    usuario_criado.refresh_from_db()  # Atualiza o banco
    assert reponse.status_code == HTTPStatus.OK
    assert usuario_criado.nome == payload["nome"]


@pytest.mark.django_db
def test_editar_usuario_nome_vazio(patch_usuario, usuario_criado):
    
    payload = {
        "nome": ""
    }

    reponse = patch_usuario(payload)
    usuario_criado.refresh_from_db()  # Atualiza o banco
    assert reponse.status_code == HTTPStatus.BAD_REQUEST
    assert reponse.data["error"] == "Campo vazio"


@pytest.mark.django_db
def test_editar_usuario_telefone_sucesso(patch_usuario, usuario_criado):
    
    payload = {
        "telefone": "999999999"
    }

    reponse = patch_usuario(payload)
    usuario_criado.refresh_from_db()  # Atualiza o banco
    assert reponse.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_editar_usuario_telefone_invalido(patch_usuario, usuario_criado):
    
    payload = {
        "telefone": "nik"
    }

    reponse = patch_usuario(payload)
    usuario_criado.refresh_from_db()  # Atualiza o banco
    assert reponse.status_code == HTTPStatus.BAD_REQUEST
    assert reponse.data["error"] == "Dados inválidos"


@pytest.mark.django_db
def test_editar_usuario_telefone_vazio(patch_usuario, usuario_criado):
    
    payload = {
        "telefone": ""
    }

    reponse = patch_usuario(payload)
    usuario_criado.refresh_from_db()  # Atualiza o banco
    assert reponse.status_code == HTTPStatus.BAD_REQUEST
    assert reponse.data["error"] == "Campo vazio"


@pytest.mark.django_db
def test_editar_usuario_data_nascimento_sucesso(patch_usuario, usuario_criado):
    
    payload = {
        "data_nascimento": "2000-10-15"
    }

    response = patch_usuario(payload)
    usuario_criado.refresh_from_db()

    assert response.status_code == HTTPStatus.OK
    assert str(usuario_criado.data_nascimento) == payload["data_nascimento"]


@pytest.mark.django_db
def test_editar_usuario_data_nascimento_invalida(patch_usuario, usuario_criado):
    
    payload = {
        "data_nascimento": "15-10-2000"
    }

    response = patch_usuario(payload)
    usuario_criado.refresh_from_db()

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.data["error"] == "Dados inválidos"


@pytest.mark.django_db
def test_editar_usuario_data_nascimento_vazia(patch_usuario, usuario_criado):
    
    payload = {
        "data_nascimento": ""
    }

    response = patch_usuario(payload)
    usuario_criado.refresh_from_db()

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.data["error"] == "Campo vazio"


@pytest.mark.django_db
def test_editar_usuario_endereco_sucesso(patch_usuario, usuario_criado):
    
    payload = {
        "endereco": "Rua das Flores, 123"
    }

    response = patch_usuario(payload)
    usuario_criado.refresh_from_db()

    assert response.status_code == HTTPStatus.OK
    assert usuario_criado.endereco == payload["endereco"]


@pytest.mark.django_db
def test_editar_usuario_endereco_invalido(patch_usuario, usuario_criado):
    
    payload = {
        "endereco": "@@@@"
    }

    response = patch_usuario(payload)
    usuario_criado.refresh_from_db()

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.data["error"] == "Dados inválidos"


@pytest.mark.django_db
def test_editar_usuario_endereco_vazio(patch_usuario, usuario_criado):
    
    payload = {
        "endereco": ""
    }

    response = patch_usuario(payload)
    usuario_criado.refresh_from_db()

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.data["error"] == "Campo vazio"


@pytest.mark.django_db
def test_deletar_usuario(delete_usuario, usuario_criado):

    response = delete_usuario()

    assert response.status_code == HTTPStatus.NO_CONTENT
    assert not User.objects.filter(username=usuario_criado.id).exists()
   
