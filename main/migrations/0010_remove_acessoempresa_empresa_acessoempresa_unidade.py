# Generated by Django 5.0.2 on 2025-06-03 19:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_orcamento_empresa_orcamento_unidade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acessoempresa',
            name='empresa',
        ),
        migrations.AddField(
            model_name='acessoempresa',
            name='unidade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.unidade'),
        ),
    ]
