from django.db import models
from main.models import empresa, cnae_empresa, cidade, uf
from django.contrib.auth.models import User
# Create your models here.



class Tomador(models.Model):
    empresa = models.ForeignKey(empresa, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cpf_cnpj = models.CharField(max_length=14)
    inscricao_estadual = models.CharField(max_length=14, null=True, blank=True)
    inscricao_municipal = models.CharField(max_length=14, null=True, blank=True)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    bairro = models.CharField(max_length=100)
    cidade = models.ForeignKey(cidade, on_delete=models.CASCADE)
    uf = models.ForeignKey(uf, on_delete=models.CASCADE)
    cep = models.CharField(max_length=8)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tomadores_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tomadores_updated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tomador'

    def __str__(self):
        return self.nome


class NotaFiscal(models.Model):
    empresa = models.ForeignKey(empresa, on_delete=models.CASCADE)
    atividade = models.ForeignKey(cnae_empresa, on_delete=models.CASCADE)
    competencia = models.DateField()
    tomador = models.ForeignKey(Tomador, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='notas_fiscais_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='notas_fiscais_updated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'nota_fiscal'

    def __str__(self):
        return f'{self.empresa.nome} - {self.tomador.nome} - {self.competencia}'
