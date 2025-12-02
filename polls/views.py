from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Curriculum, Job, User
from django.views.decorators.csrf import csrf_exempt
import json

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import ResumeUploadForm, SimpleRegisterForm
from src.pipeline.evaluator import analyze_resume

def index(request):
    return HttpResponse("Yaaaaayayyyayya!")


# Tela de Cadastro
def register_view(request):
    if request.method == 'POST':
        form = SimpleRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = User.objects.create_user(username=email, email=email, password=password)
            
            login(request, user)
            
            return redirect('upload')
    else:
        form = SimpleRegisterForm()
        
    return render(request, 'register.html', {'form': form})

# Tela de Login
def login_view(request):
    if request.method == 'POST':
        email_digitado = request.POST.get('email')
        senha_digitada = request.POST.get('password')

        try:
            # Tenta achar o usuário que tem esse email
            usuario_encontrado = User.objects.get(email=email_digitado)
            
            # Se achou, pega o username para validar a senha            
            user = authenticate(username=usuario_encontrado.username, password=senha_digitada)

            if user is not None:
                login(request, user)
                return redirect('upload') # Ou para onde ir depois de logar
            else:
                messages.error(request, 'Senha incorreta!')

        except User.DoesNotExist:
            # Se não achou ninguém
            messages.error(request, 'Email não cadastrado!')

    return render(request, 'login.html')

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')

# Tela de Upload e Pontuação
@login_required(login_url='/login/')
def upload_view(request):
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST)
        
        if form.is_valid():
            vaga = form.cleaned_data['job_description']
            texto_curriculo = form.cleaned_data['resume_text']
            
            
            score = analyze_resume(texto_curriculo, vaga)
            
            return render(request, 'score.html', {
                'score': score
            })
                
            
                
    else:
        form = ResumeUploadForm()

    return render(request, 'upload.html', {'form': form})


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

def obter_curriculo(request, curriculum_id):
    """Pega o currículo do banco de dados pelo ID."""
    curriculo = Curriculum.objects.get(id=curriculum_id)
    curriculo_data = {
        "name": curriculo.name,
        "area": curriculo.area,
        "resumo": curriculo.resumo,
        "competencias": curriculo.competencias,
        "educacao": curriculo.educacao,
    }
    return JsonResponse(curriculo_data)

@csrf_exempt
def editar_curriculo(request, curriculum_id):
    """Edita o currículo no banco de dados pelo ID."""
    if request.method == "PUT":
        data = json.loads(request.body)
        curriculo = Curriculum.objects.get(id=curriculum_id)

        curriculo.name = data.get("name", curriculo.name)
        curriculo.area = data.get("area", curriculo.area)
        curriculo.resumo = data.get("resumo", curriculo.resumo)
        curriculo.competencias = data.get("competencias", curriculo.competencias)
        curriculo.educacao = data.get("educacao", curriculo.educacao)
        curriculo.save()

        return JsonResponse({"message": "Currículo atualizado com sucesso!"})
    
@csrf_exempt
def deletar_curriculo(request, curriculum_id):
    """Deleta o currículo do banco de dados pelo ID."""
    if request.method == "DELETE":
        curriculo = Curriculum.objects.get(id=curriculum_id)
        curriculo.delete()
        return JsonResponse({"message": "Currículo deletado com sucesso!"})

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
