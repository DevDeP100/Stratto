# Generated by Django 5.0.2 on 2025-05-27 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_dre_codigo_remove_dre_nome_dre_cd_nivel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lancamento',
            name='obs',
            field=models.TextField(blank=True, null=True),
        ),
    ]
