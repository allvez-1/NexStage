from django.contrib import admin

from .models import Candidatura, Empresa, NotificacaoCandidatura, PerfilCandidato, Vaga


@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'empresa', 'area', 'prazo_candidatura', 'ativa')
    list_filter = ('ativa', 'modalidade', 'area')
    search_fields = ('titulo', 'empresa__nome_fantasia', 'area')


@admin.register(Candidatura)
class CandidaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'vaga', 'curso', 'status', 'criada_em')
    list_filter = ('status', 'criada_em')
    search_fields = ('nome', 'email', 'curso', 'vaga__titulo')

    def save_model(self, request, obj, form, change):
        status_anterior = None
        if change:
            status_anterior = Candidatura.objects.only('status').get(pk=obj.pk).status
        super().save_model(request, obj, form, change)
        if change and status_anterior != obj.status:
            NotificacaoCandidatura.objects.create(
                candidatura=obj,
                status=obj.status,
            )


@admin.register(NotificacaoCandidatura)
class NotificacaoCandidaturaAdmin(admin.ModelAdmin):
    list_display = ('candidatura', 'status', 'criada_em', 'lida')
    list_filter = ('status', 'lida', 'criada_em')
    search_fields = ('candidatura__nome', 'candidatura__vaga__titulo')
    readonly_fields = ('candidatura', 'status', 'criada_em')


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome_fantasia', 'usuario', 'cnpj', 'telefone')
    search_fields = ('nome_fantasia', 'cnpj', 'usuario__username')


@admin.register(PerfilCandidato)
class PerfilCandidatoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'curso', 'telefone')
    search_fields = ('usuario__username', 'usuario__first_name', 'usuario__last_name', 'curso')
