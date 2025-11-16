from django.db import models
from django.utils.translation import gettext_lazy as _

class Curriculum(models.Model):
    name    = models.CharField(max_length = 255)
    area    = models.CharField(max_length = 255)
    resumo = models.CharField(max_length = 50)
    competencias = models.CharField(max_length = 255)
    educacao = models.CharField(max_length = 255)

class Job(models.Model):
    idJob            = models.CharField(max_length = 4)
    link             = models.CharField(max_length = 255)
    requisitos       = models.CharField(max_length = 255)
    responsabilidade = models.CharField(max_length = 255)
    area             = models.CharField(max_length = 255)

class User(models.Model):
    idUsuario    = models.CharField(max_length = 4)
    name         = models.CharField(max_length = 255)
    adress       = models.CharField(max_length = 255)
    phone        = models.CharField(max_length = 255)
    age          = models.IntegerField()    
