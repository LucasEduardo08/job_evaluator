# import pytest
# from http import HTTPStatus
# from django.urls import reverse


# @pytest.mark.django_db
# def test_login_sucesso(api_client, usuario_criado, data):

#     payload = {
#         "username": data["username"],
#         "password": data["password"]
#     }

#     url = reverse("login")

#     response = api_client.post(url, payload, format="json")

#     print(response.data)
#     assert response.status_code == HTTPStatus.OK, "Don't possible to make login"


# @pytest.mark.django_db
# def test_login_usuario_invalido(api_client, usuario_criado, data):

#     payload = {
#         "username": "usuario_invalido",
#         "password": data["password"]
#     }

#     url = reverse("login")

#     response = api_client.post(url, payload, format="json")

#     assert response.status_code == HTTPStatus.UNAUTHORIZED, "Don't should make login with wrong username"


# @pytest.mark.django_db
# def test_login_senha_invalida(api_client, usuario_criado, data):

#     payload = {
#         "username": data["username"],
#         "password": "senha_errada"
#     }

#     url = reverse("login")

#     response = api_client.post(url, payload, format="json")

#     assert response.status_code == HTTPStatus.UNAUTHORIZED, "Don't should make login with wrong password"


# @pytest.mark.django_db
# def test_login_username_vazio(api_client, usuario_criado, data):

#     payload = {
#         "username": "",
#         "password": data["password"]
#     }

#     url = reverse("login")

#     response = api_client.post(url, payload, format="json")

#     assert response.status_code == HTTPStatus.BAD_REQUEST, "Don't should make login with null username"


# @pytest.mark.django_db
# def test_login_password_vazio(api_client, usuario_criado, data):

#     payload = {
#         "username": data["username"],
#         "password": ""
#     }

#     url = reverse("login")

#     response = api_client.post(url, payload, format="json")

#     assert response.status_code == HTTPStatus.BAD_REQUEST, "Don't should make login with null password"


# @pytest.mark.django_db
# def test_login_sem_dados(api_client, usuario_criado):

#     payload = {
#         "username": "",
#         "password": ""
#     }

#     url = reverse("login")

#     response = api_client.post(url, payload, format="json")

#     assert response.status_code == HTTPStatus.BAD_REQUEST, "Don't should make login with null username and password"


# @pytest.mark.django_db
# def test_me(api_client_autenticado, data):

#     url = reverse("me")

#     response = api_client_autenticado.get(url)

#     assert response.status_code == HTTPStatus.OK, "User don't have access"
#     assert response.data["username"] == data["username"]


# @pytest.mark.django_db
# def test_me_usuario_autenticado(api_client_autenticado, data):

#     url = reverse("teste_protegido")

#     response = api_client_autenticado.get(url)

#     assert response.status_code == HTTPStatus.OK
#     assert response.data["mensagem"] == f"Olá {data["username"]}, você está autenticado!"


# @pytest.mark.django_db
# def test_me_usuario_nao_autenticado(api_client):

#     url = reverse("teste_protegido")

#     response = api_client.get(url)

#     assert response.status_code == HTTPStatus.UNAUTHORIZED, "User have account"
