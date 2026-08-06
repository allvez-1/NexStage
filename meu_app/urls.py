from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('vagas/', views.lista_vagas, name='lista_vagas'),
    path('vagas/<int:id>/', views.detalhe_vaga, name='detalhe_vaga'),
    path('vagas/<int:id>/candidatar/', views.candidatar, name='candidatar'),
    path('publicar-vaga/', views.publicar_vaga, name='publicar_vaga'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
]
