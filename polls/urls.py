from django.urls import path
from .views import criar_curriculo, criar_vaga

from . import views

urlpatterns = [
    path("index/", views.index, name = "index"),
    path('curriculos/criar/', views.criar_curriculo, name='criar_curriculo'),
    path('vagas/criar/', views.criar_vaga, name='criar_vaga'),
    path('curriculos/avaliar/<int:curriculum_id>/<int:job_id>/', views.avaliar_curriculo, name='avaliar_curriculo'),
]
