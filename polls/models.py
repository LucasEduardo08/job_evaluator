from django.db import models
from django.utils.translation import gettext_lazy as _

class Competency(models.TextChoices):
    PROACTIVE         = _("proativo")
    RESPONSIBLE       = _("responsável")
    ORGANIZED         = _("organizado")
    TEAM_WORKER       = _("trabalho em equipe")
    EMOTION_INTELL    = _("inteligência emocional")
    LEADERSHIP        = _("liderança")
    CREATIVE          = _("criatividade")
    TIME_FLEXIBILITY  = _("flexibilidade de horário")
    TECHNICAL_PROFILE = _("perfil Técnico")
    
class Experiency(models.TextChoices):
    pass

class Area(models.TextChoices):
    COMPUTER_VISION    = _("Visão Computacional")
    MACHINE_LEARNING   = _("Aprendizado de Máquina")
    WEB_DEV            = _("Desenvolvimento Web")
    MOBILE_DEV         = _("Desenvolvimento Mobile")
    OPTIMIZATION       = _("Otimização")
    DATA_SCIENCE       = _("Ciência de Dados")
    AI_ENGINEERING     = _("Engenharia de IA")
    HARDWARE_DESIGN    = _("Design de Hardware")
    NETWORKS           = _("Redes de Computadores e Telecomunicações")
    GAME_DEV           = _("Desenvolvimento de Jogos") 


class Curriculum(models.Model):
    firstname    = models.CharField(max_length = 255)
    lastname     = models.CharField(max_length = 255)
    main_area    = models.CharField(max_length = 255, choices=Area.choices)
    competencies = models.CharField(max_length = 50)
    experiencies = models.PositiveSmallIntegerField

class JobOffer(models.Model):
    pass

class User(models.Model):
    firstname    = models.CharField(max_length = 255)
    lastname     = models.CharField(max_length = 255)
    address      = models.CharField(max_length = 255)
    phone        = models.CharField(max_length = 15)
    age          = models.PositiveSmallIntegerField()
    



