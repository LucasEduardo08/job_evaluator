from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from polls import models
from polls.models import Usuario, Curriculo, Competencia, Educacao
from django.contrib.auth.models import User
from polls.views import usuario
from django.db import transaction
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import json


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def cadastrar_curriculo(request):
    data = request.data
    user = request.user

    usuario = user.usuario

    curriculo = Curriculo.objects.create(
        usuario=usuario,
        nome_curriculo=data.get("nome_curriculo"),
        area_atuacao=data.get("area_atuacao"),
        resumo_perfil=data.get("resumo_perfil"),
        origem_curriculo=data.get("origem_curriculo"),
    )

    educacoes = data.get("educacoes", [])
    for edu in educacoes:
        Educacao.objects.create(
            curriculo=curriculo,
            instituicao=edu.get("instituicao"),
            curso=edu.get("curso"),
            nivel_educacao=edu.get("nivel_educacao"),
            data_inicio=edu.get("data_inicio"),
            data_conclusao=edu.get("data_conclusao"),
    )
        
    competencias = data.get("competencias", [])
    for comp in competencias:
        Competencia.objects.create(
            curriculo=curriculo,
            nome_competencia=comp.get("nome_competencia"),
            nivel_competencia=comp.get("nivel_competencia"),
            descricao_competencia=comp.get("descricao_competencia"),
    )

    return Response(
        {"message": "Currículo cadastrado com sucesso", "id": curriculo.id},
        status=201
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def obter_curriculo(request):
    """Pega o currículo do usuário."""
    usuario = request.user.usuario

    curriculo = Curriculo.objects.filter(usuario=usuario).first()
    if not curriculo:
        return Response({"error": "Usuário não possui currículo"}, status=404)

    educacoes = Educacao.objects.filter(curriculo=curriculo)
    competencias = Competencia.objects.filter(curriculo=curriculo)

    curriculo_data = {
        "usuario": usuario.nome,
        "nome_curriculo": curriculo.nome_curriculo,
        "area_atuacao": curriculo.area_atuacao,
        "resumo_perfil": curriculo.resumo_perfil,
        "origem_curriculo": curriculo.origem_curriculo,

        "educacoes": [
            {
                "instituicao": e.instituicao,
                "curso": e.curso,
                "nivel_educacao": e.nivel_educacao,
                "data_inicio": str(e.data_inicio),
                "data_conclusao": str(e.data_conclusao),
            }
            for e in educacoes
        ],

        "competencias": [
            {
                "nome_competencia": c.nome_competencia,
                "nivel_competencia": c.nivel_competencia,
                "descricao_competencia": c.descricao_competencia,
            }
            for c in competencias
        ]
    }

    return Response(curriculo_data)


from django.db import transaction

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def editar_curriculo(request):
    data = request.data
    usuario = request.user.usuario

    curriculo = Curriculo.objects.filter(usuario=usuario).first()
    if not curriculo:
        return Response({"error": "Usuário não possui currículo"}, status=404)

    with transaction.atomic():

        # Atualiza currículo
        curriculo.nome_curriculo = data.get("nome_curriculo", curriculo.nome_curriculo)
        curriculo.area_atuacao = data.get("area_atuacao", curriculo.area_atuacao)
        curriculo.resumo_perfil = data.get("resumo_perfil", curriculo.resumo_perfil)
        curriculo.origem_curriculo = data.get("origem_curriculo", curriculo.origem_curriculo)
        curriculo.save()

        # Atualiza competências
        Competencia.objects.filter(curriculo=curriculo).delete()
        for comp in data.get("competencias", []):
            Competencia.objects.create(
                curriculo=curriculo,
                nome_competencia=comp.get("nome_competencia"),
                nivel_competencia=comp.get("nivel_competencia"),
                descricao_competencia=comp.get("descricao_competencia"),
            )

        # Atualiza educação
        Educacao.objects.filter(curriculo=curriculo).delete()
        for edu in data.get("educacoes", []):
            Educacao.objects.create(
                curriculo=curriculo,
                instituicao=edu.get("instituicao"),
                curso=edu.get("curso"),
                nivel_educacao=edu.get("nivel_educacao"),
                data_inicio=edu.get("data_inicio"),
                data_conclusao=edu.get("data_conclusao"),
            )

    return Response({"message": "Currículo atualizado com sucesso!"})

    
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def deletar_curriculo(request):
    """Deleta o currículo do usuário"""
    usuario = request.user.usuario

    curriculo = get_object_or_404(Curriculo, usuario=usuario)

    curriculo.delete()

    return JsonResponse(
        {"message": "Currículo deletado com sucesso!"},
        status=204
    )