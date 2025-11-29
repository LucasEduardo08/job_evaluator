from django.urls import path
from .views import criar_curriculo, criar_vaga, criar_usuario, obter_usuario, avaliar_curriculo, editar_usuario

from . import views

urlpatterns = [
    path("index/", views.index, name = "index"),
    path('curriculos/criar/', views.criar_curriculo, name='criar_curriculo'),
    path('vagas/criar/', views.criar_vaga, name='criar_vaga'),
    path('curriculos/avaliar/<int:curriculum_id>/<int:job_id>/', views.avaliar_curriculo, name='avaliar_curriculo'),
    path('usuario/criar/', views.criar_usuario, name='criar_usuario'),
    path('usuario/editar/<int:user_id>/', views.editar_usuario, name='editar_usuario'),
    path('usuario/deletar/<int:user_id>/', views.deletar_usuario, name='deletar_usuario'),
    path('usuario/<int:user_id>/', views.obter_usuario, name='obter_usuario'),
]
