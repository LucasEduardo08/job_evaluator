from django.urls import path
from polls.views.auth_views import LoginView, RefreshView, MeView
from polls.views.usuario import cadastrar_usuario, obter_usuario, editar_usuario, deletar_usuario, solicitar_reset_senha, redefinir_senha
from polls.views.curriculo import cadastrar_curriculo, obter_curriculos, obter_curriculo, editar_curriculo, deletar_curriculo

from polls.views.curriculo_views import TesteProtegidoView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("refresh/", RefreshView.as_view(), name="refresh"),
    path("teste-protegido/", TesteProtegidoView.as_view()),
    path("me/", MeView.as_view(), name="me"),

    path("criar_usuario/", cadastrar_usuario, name="criar_usuario"),
    path("usuario/me/", obter_usuario),
    path("usuario/editar/me/", editar_usuario),
    path("usuario/deletar/me/", deletar_usuario),
    path("auth/reset-senha/", solicitar_reset_senha),
    path("auth/redefinir-senha/", redefinir_senha),

    path("criar_curriculo/", cadastrar_curriculo, name="criar_curriculo"),
    path("curriculo/me/", obter_curriculos), # Todos os currículos do usuário
    path("curriculo/<int:id>/", obter_curriculo), # Currículo específico
    path("curriculo/editar/<int:id>/", editar_curriculo),
    path("curriculo/deletar/<int:id>/", deletar_curriculo),
]