from django.contrib import admin
from .models import (
    empresa, unidade, centro_resultado, 
    dre, dfc, plano_contas, lancamento
)

@admin.register(empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cnpj', 'email', 'telefone', 'created_at')
    search_fields = ('nome', 'cnpj', 'email')
    list_filter = ('created_at',)

@admin.register(unidade)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'empresa', 'sigla', 'created_at')
    search_fields = ('nome', 'sigla')
    list_filter = ('empresa', 'created_at')

@admin.register(centro_resultado)
class CentroResultadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'empresa', 'codigo', 'nivel', 'created_at')
    search_fields = ('codigo', 'nome', 'nivel')
    list_filter = ('empresa', 'nivel', 'created_at')

@admin.register(dre)
class DreAdmin(admin.ModelAdmin):
    list_display = ('id', 'cd_nivel', 'nivel', 'cd_nivel2', 'nivel2', 'empresa', 'created_at')
    search_fields = ('cd_nivel', 'nivel', 'cd_nivel2', 'nivel2')
    list_filter = ('empresa', 'created_at')

@admin.register(dfc)
class DfcAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nome', 'empresa', 'created_at')
    search_fields = ('codigo', 'nome')
    list_filter = ('empresa', 'created_at')

@admin.register(plano_contas)
class PlanoContasAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nome', 'empresa', 'nivel1', 'nivel2', 'dre', 'dfc', 'created_at')
    search_fields = ('codigo', 'nome', 'nivel1', 'nivel2')
    list_filter = ('empresa', 'dre', 'dfc', 'created_at')

@admin.register(lancamento)
class LancamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'empresa', 'unidade', 'centro_resultado', 'plano_contas', 'data', 'valor', 'created_at')
    search_fields = ('obs',)
    list_filter = ('empresa', 'unidade', 'centro_resultado', 'plano_contas', 'data', 'created_at')
    date_hierarchy = 'data'
