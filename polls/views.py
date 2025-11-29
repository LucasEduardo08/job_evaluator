from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Curriculum, Job, User
from django.views.decorators.csrf import csrf_exempt
import json
from src.pipeline.evaluator import analyze_resume

def index(request):
    return HttpResponse("Yaaaaayayyyayya!")

# Create your views here

@csrf_exempt
def criar_curriculo(request):
    if request.method == "POST":
        data = json.loads(request.body)

        curriculo = Curriculum.objects.create(
            name=data.get("name"),
            area=data.get("area"),
            resumo=data.get("resumo"),
            competencias=data.get("competencias"),
            educacao=data.get("educacao")
        )

        return JsonResponse({"message": "Currículo criado com sucesso!"})

@csrf_exempt
def criar_vaga(request):
    if request.method == "POST":
        data = json.loads(request.body)

        vaga = Job.objects.create(
            idJob=data.get("idJob"),
            link=data.get("link"),
            area=data.get("area"),
            requisitos=data.get("requisitos"),
            responsabilidade=data.get("responsabilidade")
        )

        return JsonResponse({"message": "Vaga criada com sucesso!", "id": vaga.id})

@csrf_exempt
def criar_usuario(request):
    if request.method == "POST":
        data = json.loads(request.body)

        usuario = User.objects.create(
            idUsuario=data.get("idUsuario"),
            name=data.get("name"),
            adress=data.get("adress"),
            phone=data.get("phone"),
            age=data.get("age")
        )

        return JsonResponse({"message": "Usuário criado com sucesso!"})
    
def obter_usuario(request, user_id):
    """Pega o usuário do banco de dados pelo ID."""
    usuario = User.objects.get(id=user_id)
    usuario_data = {
        "idUsuario": usuario.idUsuario,
        "name": usuario.name,
        "adress": usuario.adress,
        "phone": usuario.phone,
        "age": usuario.age,
    }
    return JsonResponse(usuario_data)

@csrf_exempt
def editar_usuario(request, user_id):
    """Edita o usuário no banco de dados pelo ID."""
    if request.method == "PUT":
        data = json.loads(request.body)
        usuario = User.objects.get(id=user_id)

        usuario.idUsuario = data.get("idUsuario", usuario.idUsuario)
        usuario.name = data.get("name", usuario.name)
        usuario.adress = data.get("adress", usuario.adress)
        usuario.phone = data.get("phone", usuario.phone)
        usuario.age = data.get("age", usuario.age)
        usuario.save()

        return JsonResponse({"message": "Usuário atualizado com sucesso!"})
    
@csrf_exempt
def deletar_usuario(request, user_id):
    """Deleta o usuário do banco de dados pelo ID."""
    if request.method == "DELETE":
        usuario = User.objects.get(id=user_id)
        usuario.delete()
        return JsonResponse({"message": "Usuário deletado com sucesso!"})

def avaliar_curriculo(request, curriculum_id, job_id):
    """Pega o currículo e a vaga do banco e envia pro modelo fazer o score."""

    curriculo = Curriculum.objects.get(id=curriculum_id)
    vaga = Job.objects.get(id=job_id)

    cv_text = f"""
    Nome: {curriculo.name}
    Resumo: {curriculo.resumo}
    Area: {curriculo.area}
    Competências: {curriculo.competencias}
    Educação: {curriculo.educacao}
    """
    job_dict = {
        "link": vaga.link,
        "area": vaga.area,
        "requisitos": vaga.requisitos,
        "responsabilidade": vaga.responsabilidade,
    }

    resultado = analyze_resume(cv=cv_text, job=job_dict)

    return JsonResponse(resultado, safe=False)
