from django.db import models
from django.contrib.auth.models import User, Group
from main.models import empresa

# Create your models here.



class Link(models.Model):
    empresa = models.ForeignKey(empresa, on_delete=models.CASCADE)
    desc = models.CharField(max_length=40, default='')
    link = models.CharField(max_length=400)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='links_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='links_updated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        # Managed = Trues
        db_table = 'Link'

    def __str__(self):
        return '{} - {} '.format(self.empresa.nome, self.desc)

class Acesso(models.Model):
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    link = models.ForeignKey(Link, on_delete=models.PROTECT)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='acessos_created')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='acessos_updated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Acesso'
        ordering = ['group__name']

    def __str__(self):
        return f'{self.group.name} - {self.link.desc}'

