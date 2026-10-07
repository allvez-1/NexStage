from django.contrib import admin

from .models import Candidatura, Empresa, PerfilCandidato, Vaga


@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'empresa', 'area', 'prazo_candidatura', 'ativa')
    list_filter = ('ativa', 'modalidade', 'area')
    search_fields = ('titulo', 'empresa__nome_fantasia', 'area')


@admin.register(Candidatura)
class CandidaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'vaga', 'curso', 'status', 'criada_em')
    list_editable = ('status',)
    list_filter = ('status', 'criada_em')
    search_fields = ('nome', 'email', 'curso', 'vaga__titulo')


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome_fantasia', 'usuario', 'cnpj', 'telefone')
    search_fields = ('nome_fantasia', 'cnpj', 'usuario__username')


@admin.register(PerfilCandidato)
class PerfilCandidatoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'curso', 'telefone')
    search_fields = ('usuario__username', 'usuario__first_name', 'usuario__last_name', 'curso')
