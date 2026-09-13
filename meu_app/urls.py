from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('vagas/', views.lista_vagas, name='lista_vagas'),
    path('vagas/<int:id>/', views.detalhe_vaga, name='detalhe_vaga'),
    path('vagas/<int:id>/candidatar/', views.candidatar, name='candidatar'),
    path('entrar/candidato/', views.login_candidato, name='login_candidato'),
    path('entrar/empresa/', views.login_empresa, name='login_empresa'),
    path('cadastro/candidato/', views.cadastro_candidato, name='cadastro_candidato'),
    path('cadastro/empresa/', views.cadastro_empresa, name='cadastro_empresa'),
    path('sair/', views.sair, name='sair'),
    path('painel/candidato/', views.painel_candidato, name='painel_candidato'),
    path('painel/candidato/perfil/', views.editar_perfil_candidato, name='editar_perfil_candidato'),
    path('painel/empresa/', views.painel_empresa, name='painel_empresa'),
    path('painel/empresa/perfil/', views.editar_empresa, name='editar_empresa'),
    path('painel/empresa/vagas/nova/', views.publicar_vaga, name='publicar_vaga'),
    path('painel/empresa/vagas/<int:id>/editar/', views.editar_vaga, name='editar_vaga'),
    path('painel/empresa/vagas/<int:id>/excluir/', views.excluir_vaga, name='excluir_vaga'),
    path('painel/empresa/vagas/<int:id>/candidatos/', views.candidatos_vaga, name='candidatos_vaga'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
]
