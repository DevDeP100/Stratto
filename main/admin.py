from django.contrib import admin
from .models import (
    empresa, unidade, centro_resultado, 
    dre, dfc, plano_contas, lancamento, Orcamento, AcessoEmpresa
)
from django.utils.html import format_html
from django.urls import reverse
from django.db.models import Q
from django.contrib.admin import SimpleListFilter

class AccessFilteredListFilter(SimpleListFilter):
    def lookups(self, request, model_admin):
        if request.user.is_superuser:
            return self.get_all_lookups()
        
        # Get user's accessible units and companies
        user_units = AcessoEmpresa.objects.filter(usuario=request.user).values_list('unidade_id', 'unidade__empresa_id')
        empresa_ids = list(set(empresa_id for _, empresa_id in user_units))
        unidade_ids = list(set(unidade_id for unidade_id, _ in user_units))
        
        return self.get_filtered_lookups(empresa_ids, unidade_ids)

    def get_all_lookups(self):
        raise NotImplementedError("Subclasses must implement get_all_lookups()")

    def get_filtered_lookups(self, empresa_ids, unidade_ids):
        raise NotImplementedError("Subclasses must implement get_filtered_lookups()")

class UnidadeFilter(AccessFilteredListFilter):
    title = 'Unidade'
    parameter_name = 'unidade'

    def get_all_lookups(self):
        return [(u.id, u.nome) for u in unidade.objects.all()]

    def get_filtered_lookups(self, empresa_ids, unidade_ids):
        return [(u.id, u.nome) for u in unidade.objects.filter(id__in=unidade_ids)]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(unidade_id=self.value())
        return queryset

class EmpresaFilter(AccessFilteredListFilter):
    title = 'Empresa'
    parameter_name = 'empresa'

    def get_all_lookups(self):
        return [(e.id, e.nome) for e in empresa.objects.all()]

    def get_filtered_lookups(self, empresa_ids, unidade_ids):
        return [(e.id, e.nome) for e in empresa.objects.filter(id__in=empresa_ids)]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(empresa_id=self.value())
        return queryset

class CentroResultadoFilter(AccessFilteredListFilter):
    title = 'Centro de Resultado'
    parameter_name = 'centro_resultado'

    def get_all_lookups(self):
        return [(cr.id, cr.nome) for cr in centro_resultado.objects.all()]

    def get_filtered_lookups(self, empresa_ids, unidade_ids):
        return [(cr.id, cr.nome) for cr in centro_resultado.objects.filter(empresa_id__in=empresa_ids)]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(centro_resultado_id=self.value())
        return queryset

class PlanoContasFilter(AccessFilteredListFilter):
    title = 'Plano de Contas'
    parameter_name = 'plano_contas'

    def get_all_lookups(self):
        return [(pc.id, pc.nome) for pc in plano_contas.objects.all()]

    def get_filtered_lookups(self, empresa_ids, unidade_ids):
        return [(pc.id, pc.nome) for pc in plano_contas.objects.filter(empresa_id__in=empresa_ids)]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(plano_contas_id=self.value())
        return queryset

class DreFilter(AccessFilteredListFilter):
    title = 'DRE'
    parameter_name = 'dre'

    def get_all_lookups(self):
        return [(d.id, d.nivel) for d in dre.objects.all()]

    def get_filtered_lookups(self, empresa_ids, unidade_ids):
        return [(d.id, d.nivel) for d in dre.objects.filter(empresa_id__in=empresa_ids)]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(dre_id=self.value())
        return queryset

class DfcFilter(AccessFilteredListFilter):
    title = 'DFC'
    parameter_name = 'dfc'

    def get_all_lookups(self):
        return [(d.id, d.nome) for d in dfc.objects.all()]

    def get_filtered_lookups(self, empresa_ids, unidade_ids):
        return [(d.id, d.nome) for d in dfc.objects.filter(empresa_id__in=empresa_ids)]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(dfc_id=self.value())
        return queryset

class CompanyFilteredAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        # Get units the user has access to
        user_units = AcessoEmpresa.objects.filter(usuario=request.user).values_list('unidade_id', 'unidade__empresa_id')
        # Extract distinct empresa IDs from user_units
        empresa_ids = list(set(empresa_id for _, empresa_id in user_units))
        unidade_ids = list(set(unidade_id for unidade_id, _ in user_units))
        
        # Check if the model has unidade field directly
        if hasattr(self.model, 'unidade'):
            print(unidade_ids)
            return qs.filter(unidade_id__in=unidade_ids)
        # If model has empresa field, filter through it
        elif hasattr(self.model, 'empresa'):
            print(empresa_ids)
            return qs.filter(empresa__id__in=empresa_ids)
        
        return qs

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if request.user.is_superuser:
            return super().formfield_for_foreignkey(db_field, request, **kwargs)

        # Get user's accessible units and companies
        user_units = AcessoEmpresa.objects.filter(usuario=request.user).values_list('unidade_id', 'unidade__empresa_id')
        # Extract distinct empresa IDs from user_units
        empresa_ids = list(set(empresa_id for _, empresa_id in user_units))
        unidade_ids = list(set(unidade_id for unidade_id, _ in user_units))

        print(empresa_ids)
        # Filter unidade choices
        if db_field.name == "unidade":
            kwargs["queryset"] = unidade.objects.filter(id__in=unidade_ids)
        # Filter empresa choices
        elif db_field.name == "empresa":
            kwargs["queryset"] = empresa.objects.filter(id__in=empresa_ids)
        # Filter centro_resultado choices
        elif db_field.name == "centro_resultado":
            kwargs["queryset"] = centro_resultado.objects.filter(empresa_id__in=empresa_ids)
        # Filter plano_contas choices
        elif db_field.name == "plano_contas":
            kwargs["queryset"] = plano_contas.objects.filter(empresa_id__in=empresa_ids)
        # Filter dre choices
        elif db_field.name == "dre":
            kwargs["queryset"] = dre.objects.filter(empresa_id__in=empresa_ids)
        # Filter dfc choices
        elif db_field.name == "dfc":
            kwargs["queryset"] = dfc.objects.filter(empresa_id__in=empresa_ids)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    

@admin.register(empresa)
class EmpresaAdmin(CompanyFilteredAdmin):
    list_display = ('id', 'nome', 'cnpj', 'email', 'telefone')
    search_fields = ('nome', 'cnpj', 'email')
    list_filter = ('created_at', 'created_by', 'updated_by')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')

@admin.register(unidade)
class UnidadeAdmin(CompanyFilteredAdmin):
    list_display = ('id', 'nome', 'empresa', 'sigla')
    search_fields = ('nome', 'sigla')
    list_filter = (EmpresaFilter, 'created_at', 'created_by', 'updated_by')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')

@admin.register(centro_resultado)
class CentroResultadoAdmin(CompanyFilteredAdmin):
    list_display = ('id', 'nome', 'empresa', 'codigo', 'nivel')
    search_fields = ('codigo', 'nome', 'nivel')
    list_filter = (EmpresaFilter, 'nivel', 'created_at', 'created_by', 'updated_by')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')

@admin.register(dre)
class DreAdmin(CompanyFilteredAdmin):
    list_display = ('id', 'cd_nivel', 'nivel', 'cd_nivel2', 'nivel2', 'empresa')
    search_fields = ('cd_nivel', 'nivel', 'cd_nivel2', 'nivel2')
    list_filter = (EmpresaFilter,)
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')

@admin.register(dfc)
class DfcAdmin(CompanyFilteredAdmin):
    list_display = ('id', 'codigo', 'nome', 'empresa')
    search_fields = ('codigo', 'nome')
    list_filter = (EmpresaFilter,)
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')

@admin.register(plano_contas)
class PlanoContasAdmin(CompanyFilteredAdmin):
    list_display = ('id', 'codigo', 'nome', 'empresa', 'nivel1', 'nivel2', 'dre', 'dfc')
    search_fields = ('codigo', 'nome', 'nivel1', 'nivel2')
    list_filter = (EmpresaFilter, DreFilter, DfcFilter)
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')

@admin.register(lancamento)
class LancamentoAdmin(CompanyFilteredAdmin):
    list_display = ('id', 'unidade', 'centro_resultado', 'plano_contas', 'data', 'valor')
    search_fields = ('obs',)
    list_filter = (UnidadeFilter, CentroResultadoFilter, PlanoContasFilter, 'data')
    date_hierarchy = 'data'
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')

@admin.register(Orcamento)
class OrcamentoAdmin(CompanyFilteredAdmin):
    list_display = ('id', 'unidade', 'data', 'conta', 'valor')
    search_fields = ('unidade__nome', 'conta__nome')
    list_filter = (UnidadeFilter, 'data', 'conta')
    date_hierarchy = 'data'
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')

@admin.register(AcessoEmpresa)
class AcessoEmpresaAdmin(CompanyFilteredAdmin):
    list_display = ('id', 'unidade', 'usuario')
    search_fields = ('unidade__nome', 'usuario__username')
    list_filter = ('unidade', 'usuario')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
