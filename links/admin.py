from django.contrib import admin
from django.utils.html import format_html
from .models import Link, Acesso
from datetime import datetime
# Register your models here.

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'desc', 'link_clicavel')
    search_fields = ('empresa__nome', 'desc')
    list_filter = ('empresa', 'created_by', 'updated_by')
    readonly_fields = ('created_by', 'updated_by', 'created_at', 'updated_at')

    def link_clicavel(self, obj):
        return format_html('<a href="{}" target="_blank">Acessar Painel</a>', obj.link)
    link_clicavel.short_description = 'Link'

    def save_model(self, request, obj, form, change):
        if not change:  # Se for uma criação
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        # Filtra os links baseado nos grupos do usuário
        user_groups = request.user.groups.all()
        return qs.filter(acesso__group__in=user_groups).distinct()

@admin.register(Acesso)
class AcessoAdmin(admin.ModelAdmin):
    list_display = ('group', 'link', 'created_by', 'updated_by', 'created_at', 'updated_at')
    search_fields = ('group__name', 'link__desc')
    list_filter = ('group', 'link__empresa', 'created_by', 'updated_by')
    readonly_fields = ('created_by', 'updated_by', 'created_at', 'updated_at')

    def save_model(self, request, obj, form, change):
        if not change:  # Se for uma criação
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)



