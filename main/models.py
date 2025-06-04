from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='empresas_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='empresas_updated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'empresa'

    def __str__(self):
        return self.nome


class unidade(models.Model):
    nome = models.CharField(max_length=100)
    empresa = models.ForeignKey(empresa, on_delete=models.SET_NULL, null=True)
    sigla = models.CharField(max_length=10)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='unidades_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='unidades_updated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'unidade'

    def __str__(self):
        return self.nome

class centro_resultado(models.Model):
    nome = models.CharField(max_length=100)
    empresa = models.ForeignKey(empresa, on_delete=models.SET_NULL, null=True)
    codigo = models.CharField(max_length=100)
    nivel = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='centros_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='centros_updated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'centro_resultado'

    def __str__(self):
        return self.nome
    

class dre(models.Model):
    cd_nivel = models.CharField(max_length=100)
    nivel = models.CharField(max_length=100)
    cd_nivel2 = models.CharField(max_length=100)
    nivel2 = models.CharField(max_length=100)
    empresa = models.ForeignKey(empresa, on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='dres_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='dres_updated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'dre'

    def __str__(self):
        return self.nivel
    
class dfc(models.Model):
    codigo = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    empresa = models.ForeignKey(empresa, on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='dfcs_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='dfcs_updated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'dfc'

    def __str__(self):
        return self.nome
    
        
class plano_contas(models.Model):
    codigo = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    empresa = models.ForeignKey(empresa, on_delete=models.SET_NULL, null=True)
    nivel1 = models.CharField(max_length=100)
    nivel2 = models.CharField(max_length=100)
    dre = models.ForeignKey(dre, on_delete=models.SET_NULL, null=True)
    dfc = models.ForeignKey(dfc, on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='planos_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='planos_updated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'plano_contas'

    def __str__(self):
        return self.nome
    

class lancamento(models.Model):
    unidade = models.ForeignKey(unidade, on_delete=models.SET_NULL, null=True)
    centro_resultado = models.ForeignKey(centro_resultado, on_delete=models.SET_NULL, null=True)
    plano_contas = models.ForeignKey(plano_contas, on_delete=models.SET_NULL, null=True)
    data = models.DateField()
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    obs = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='lancamentos_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='lancamentos_updated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'lancamento'

    def __str__(self):
        return f'{self.data} - {self.valor}'
    

    
class Orcamento(models.Model):
    unidade = models.ForeignKey(unidade, on_delete=models.SET_NULL, null=True)
    data = models.DateField()
    conta = models.ForeignKey(plano_contas, on_delete=models.SET_NULL, null=True)
    valor = models.FloatField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='orcamentos_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='orcamentos_updated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'orcamento'
    
    def __str__(self):
        return f'{self.unidade.nome if self.unidade else ""} - {self.data} - {self.conta.nome if self.conta else ""}'


class AcessoEmpresa(models.Model):
    unidade = models.ForeignKey(unidade, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='acessosEmpresa_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='acessosEmpresa_updated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
        db_table = 'acesso_empresa'

    def __str__(self):
        return f'{self.unidade.nome if self.unidade else ""} - {self.usuario.username if self.usuario else ""}'