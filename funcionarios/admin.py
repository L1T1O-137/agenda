from django.contrib import admin
from .models import Funcionario

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    fields = ('nome', 'fone', 'email', 'funcao', 'data_admissao', 'foto', 'fotografia')
    list_display = ('nome', 'foto', 'email', 'funcao')
    readonly_fields = ['fotografia']
    search_fields = ('nome', 'fone',)
    list_filter = ('funcao',)

    def fotografia(selfself, obj):
        if obj.foto:
            return format_html('<img width="75px" src="{}" />', obj.foto.url)
        pass