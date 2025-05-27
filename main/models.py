from django.db import models

# Create your models here.
class empresa(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    telefone = models.CharField(max_length=255, null=True, blank=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class unidade(models.Model):
    empresa = models.ForeignKey(empresa, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class centro_resultado(models.Model):
    empresa = models.ForeignKey(empresa, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    nivel = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    

class dre(models.Model):
    empresa = models.ForeignKey(empresa, on_delete=models.CASCADE)
    cd_nivel = models.CharField(max_length=255, null=True, blank=True)
    nivel = models.CharField(max_length=255, null=True, blank=True)
    cd_nivel2 = models.CharField(max_length=255, null=True, blank=True)
    nivel2 = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nivel
    
class dfc(models.Model):
    empresa = models.ForeignKey(empresa, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    
        
class plano_contas(models.Model):
    empresa = models.ForeignKey(empresa, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    nivel1 = models.CharField(max_length=255, null=True, blank=True)
    nivel2 = models.CharField(max_length=255, null=True, blank=True)
    dre = models.ForeignKey(dre, on_delete=models.CASCADE, null=True, blank=True)
    dfc = models.ForeignKey(dfc, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    

class lancamento(models.Model):
    empresa = models.ForeignKey(empresa, on_delete=models.CASCADE)
    unidade = models.ForeignKey(unidade, on_delete=models.CASCADE)
    centro_resultado = models.ForeignKey(centro_resultado, on_delete=models.CASCADE)
    plano_contas = models.ForeignKey(plano_contas, on_delete=models.CASCADE)
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    obs  = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plano_contas.nome
    