from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from polls.models import Usuario
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import json


@api_view(["POST"])
@permission_classes([AllowAny])
def cadastrar_usuario(request):
    data = request.data

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return Response(
            {"error": "username, email e password são obrigatórios"},
            status=400
        )

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username já existe"}, status=400)

    if User.objects.filter(email=email).exists():
        return Response({"error": "Email já existe"}, status=400)

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )

    usuario = Usuario.objects.create(
        user=user,
        nome=data.get("nome"),
        telefone=data.get("telefone"),
        endereco=data.get("endereco"),
        data_nascimento=data.get("data_nascimento")
    )

    return Response(
        {"message": "Usuário cadastrado com sucesso", "id": usuario.id},
        status=201
    )



@api_view(["GET"])
@permission_classes([IsAuthenticated])
def obter_usuario(request):
    """Pega o usuário."""
    usuario = request.user.usuario
    user = request.user

    usuario_data = {
        "nome": usuario.nome,
        "email": user.email,
        "telefone": usuario.telefone,
        "endereco": usuario.endereco,
        "data_nascimento": str(usuario.data_nascimento),
    }
    return JsonResponse(usuario_data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def editar_usuario(request):
    """Edita o usuário"""
    data = request.data
    usuario = request.user.usuario
    user = request.user

    usuario.nome = data.get("nome", usuario.nome)
    usuario.telefone = data.get("telefone", usuario.telefone)
    usuario.endereco = data.get("endereco", usuario.endereco)
    usuario.data_nascimento = data.get("data_nascimento", usuario.data_nascimento)

    user.email = data.get("email", user.email)

    usuario.save()
    user.save()

    return JsonResponse({"message": "Usuário atualizado com sucesso!"})


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def deletar_usuario(request):
    """Deleta o usuário"""
    user = request.user
    user.delete()

    return JsonResponse({"message": "Usuário deletado com sucesso!"})