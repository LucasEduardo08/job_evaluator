from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Curriculum, Job
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
