from django.contrib import admin
from .models import Moto

@admin.register(Moto)
class MotoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'ano', 'cor', 'preco')
    search_fields = ('marca', 'modelo', 'cor')
    list_filter = ('marca', 'ano', 'cor')
