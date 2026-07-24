from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('estoque/', views.lista_motos, name='lista_motos'),
    path('novo/', views.criar_moto, name='criar_moto'),
    path('editar/<int:id>/', views.editar_moto, name='editar_moto'),
    path('deletar/<int:id>/', views.deletar_moto, name='deletar_moto'),
    path('detalhe/<int:id>/', views.detalhe_moto, name='detalhe_moto')
]
