from django.contrib import admin

from .models import Candidatura, Vaga


@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'empresa', 'area', 'prazo_candidatura', 'ativa')
    list_filter = ('ativa', 'modalidade', 'area')
    search_fields = ('titulo', 'empresa', 'area')


@admin.register(Candidatura)
class CandidaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'vaga', 'curso', 'criada_em')
    search_fields = ('nome', 'email', 'curso')
