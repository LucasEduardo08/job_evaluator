from django.urls import path

from . import views

urlpatterns = [    
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),    
    path('logout/', views.logout_view, name='logout'),
    path('upload/', views.upload_view, name='upload'),
    path("index/", views.index, name = "index"),
    path('curriculos/criar/', views.criar_curriculo, name='criar_curriculo'),
    path('curriculo/editar/<int:curriculum_id>/', views.editar_curriculo, name='editar_curriculo'),
    path('curriculo/deletar/<int:curriculum_id>/', views.deletar_curriculo, name='deletar_curriculo'),
    path('curriculo/<int:curriculum_id>/', views.obter_curriculo, name='obter_curriculo'),
    path('vagas/criar/', views.criar_vaga, name='criar_vaga'),
    path('curriculos/avaliar/<int:curriculum_id>/<int:job_id>/', views.avaliar_curriculo, name='avaliar_curriculo'),
    path('usuario/criar/', views.criar_usuario, name='criar_usuario'),
    path('usuario/editar/<int:user_id>/', views.editar_usuario, name='editar_usuario'),
    path('usuario/deletar/<int:user_id>/', views.deletar_usuario, name='deletar_usuario'),
    path('usuario/<int:user_id>/', views.obter_usuario, name='obter_usuario'),
    
]
