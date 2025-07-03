from django.contrib import admin
from .models import NotaFiscal, Tomador
# Register your models here.
@admin.register(NotaFiscal)
class NotaFiscalAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'tomador', 'competencia', 'valor', 'descricao')
    list_filter = ('empresa', 'tomador', 'competencia')
    search_fields = ('empresa__nome', 'tomador__nome', 'competencia')


@admin.register(Tomador)
class TomadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')
    search_fields = ('nome', 'email', 'telefone')



