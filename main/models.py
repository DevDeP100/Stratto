from django.db import models
from django.contrib.auth.models import User


class uf(models.Model):
    codigo_uf = models.IntegerField(unique=True)
    uf = models.CharField(max_length=2)
    nome = models.CharField(max_length=100)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    regiao = models.CharField(max_length=100, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='ufs_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='ufs_updated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'uf'
        ordering = ('nome',)

    def __str__(self):
        return self.nome
    
class cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.ForeignKey(uf, on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='cidades_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='cidades_updated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cidade'

    def __str__(self):
        return self.nome

# Create your models here.
class empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    inscricao_estadual = models.CharField(max_length=14, null=True, blank=True)
    inscricao_municipal = models.CharField(max_length=14, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    numero = models.CharField(max_length=10, null=True, blank=True)
    cep = models.CharField(max_length=8, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    cidade = models.ForeignKey(cidade, on_delete=models.SET_NULL, null=True, blank=True)
    uf = models.ForeignKey(uf, on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='empresas_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='empresas_updated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'empresa'

    def __str__(self):
        return self.nome
    
class cnae_empresa(models.Model):
    empresa = models.ForeignKey(empresa, on_delete=models.SET_NULL, null=True)
    cnae = models.CharField(max_length=100)
    principal = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='cnae_empresas_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='cnae_empresas_updated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cnae_empresa'

    def __str__(self):
        return self.cnae
    


    
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
    cd_nivel = models.CharField(max_length=100, null=True, blank=True)
    nivel = models.CharField(max_length=100, null=True, blank=True)
    cd_nivel2 = models.CharField(max_length=100, null=True, blank=True)
    nivel2 = models.CharField(max_length=100, null=True, blank=True)
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
    dre = models.ForeignKey(dre, on_delete=models.SET_NULL, null=True, blank=True)
    dfc = models.ForeignKey(dfc, on_delete=models.SET_NULL, null=True, blank=True)
    ativo = models.BooleanField(default=True)
    natureza = models.IntegerField(default=1)
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