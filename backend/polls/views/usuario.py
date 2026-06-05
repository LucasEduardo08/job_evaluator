import re
from django.http import JsonResponse
from polls.models import Usuario, PasswordResetToken
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from django.contrib.auth.hashers import make_password
from email_validator import validate_email, EmailNotValidError


def validar_email(email):
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False


@api_view(["POST"])
@permission_classes([AllowAny])
def cadastrar_usuario(request):
    data = request.data

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    nome = data.get("nome")
    telefone = data.get("telefone")
    endereco = data.get("endereco")
    data_nascimento = data.get("data_nascimento")

    if not username or not email or not password or not nome or not telefone or not endereco or not data_nascimento:
        return Response({"error": "Some data is missing"}, status=400)
    
    if not validar_email(email):
        return Response(
            {"error": "Invalid email address"}, status=400)

    regexNome = r"^[A-Za-zÀ-ÖØ-öø-ÿ ]+$"
    if not re.match(regexNome, nome):
        return Response({"error": "Invalid name"}, status=400)
    
    regexTelefone = r"^\(\d{2}\) \d{5}-\d{4}$"
    if not re.match(regexTelefone, telefone):
        return Response({"error": "Invalid phone number"}, status=400)
    
    #regexEndereco = r"^[A-Za-z0-9, ]+$"
    #if not re.match(regexEndereco, endereco):
    #    return Response({"error": "Invalid address"}, status=400)

    regexDataNascimento = r"^\d{4}-\d{2}-\d{2}$"
    if not re.match(regexDataNascimento, data_nascimento):
        return Response({"error": "Invalid date"}, status=400)


    if len(password) < 8:
        return Response({"error": "Password must have at least 8 characters"}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists"}, status=400)

    if User.objects.filter(email=email).exists():
        return Response({"error": "Email already exists"}, status=400)

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
        {"message": "User created successfully", "email": usuario.user.email},
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
        "username": user.username,
        "email": user.email,
        "telefone": usuario.telefone,
        "endereco": usuario.endereco,
        "data_nascimento": str(usuario.data_nascimento),
    }
    return Response({"usuario": usuario_data}, status=200)


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

    return Response({"message": "User updated successfully"}, status=200)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def deletar_usuario(request):
    """Deleta o usuário"""
    user = request.user
    user.delete()

    return JsonResponse({"message": "Usuário deletado com sucesso!"})


@api_view(["POST"])
def solicitar_reset_senha(request):
    email = request.data.get("email")

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        # Segurança: não revelar se o email existe
        return Response(
            {"message": "Se o email existir, enviaremos instruções."},
            status=200
        )

    token = PasswordResetToken.objects.create(user=user)

    link = f"http://localhost:8501/resetar-senha?token={token.token}"

    send_mail(
        subject="Redefinição de senha",
        message=f"Clique no link para redefinir sua senha:\n{link}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        fail_silently=False,
    )

    return Response({"message": "Email enviado com sucesso!"})


@api_view(["POST"])
def redefinir_senha(request):
    token_str = request.data.get("token")
    nova_senha = request.data.get("nova_senha")

    try:
        token = PasswordResetToken.objects.get(token=token_str)
    except PasswordResetToken.DoesNotExist:
        return Response({"error": "Token inválido"}, status=400)

    if token.expirado():
        return Response({"error": "Token expirado"}, status=400)

    user = token.user
    user.set_password(nova_senha)
    user.save()

    token.delete()

    return Response({"message": "Senha atualizada com sucesso!"})

