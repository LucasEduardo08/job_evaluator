from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Usuario(models.Model):
    user                     = models.OneToOneField(User, on_delete=models.CASCADE)
    nome                     = models.TextField()
    endereco                 = models.TextField()
    telefone                 = models.CharField(max_length = 17)
    data_nascimento          = models.DateField()


class Curriculo(models.Model):
    area_atuacao            = models.TextField()
    resumo_perfil           = models.TextField()
    origem_curriculo        = models.CharField(max_length = 255)
    usuario                 = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_criacao            = models.DateField(auto_now_add=True)
    nome_curriculo          = models.CharField(max_length = 255)


class Vaga(models.Model):
    empresa                  = models.CharField(max_length = 100)
    data_publicacao          = models.DateField(auto_now_add=True)
    link                     = models.TextField()
    titulo                   = models.CharField(max_length = 255)
    localizacao              = models.CharField(max_length = 100)
    nivel                    = models.CharField(max_length = 30)
    descricao                = models.TextField()
    responsabilidades        = models.TextField()
    requisitos_obrigatorios  = models.TextField()
    diferencial              = models.TextField()
    requisitos_desejaveis   = models.TextField()


class Candidatura(models.Model):
    STATUS_CHOICES = [
        ("enviada", "Enviada"),
        ("em_analise", "Em análise"),
        ("aprovada", "Aprovada"),
        ("rejeitada", "Rejeitada"),
    ]

    usuario                 = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    vaga                    = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    curriculo               = models.ForeignKey(Curriculo, on_delete=models.CASCADE)
    data_candidatura        = models.DateField(auto_now_add=True)
    status                  = models.CharField(max_length = 20, choices=STATUS_CHOICES, default="enviada")
    score                   = models.DecimalField(max_digits=5, decimal_places=2)
    recomendacoes           = models.TextField()


class Competencia(models.Model):
    nome_competencia          = models.CharField(max_length = 100)
    nivel_competencia         = models.CharField(max_length = 50)
    curriculo                 = models.ForeignKey(Curriculo, on_delete=models.CASCADE)
    descricao_competencia     = models.TextField()


class Educacao(models.Model):
    instituicao               = models.CharField(max_length = 255)
    curso                     = models.CharField(max_length = 255)
    nivel_educacao            = models.CharField(max_length = 100)
    data_inicio               = models.DateField()
    data_conclusao            = models.DateField()
    curriculo                 = models.ForeignKey(Curriculo, on_delete=models.CASCADE)