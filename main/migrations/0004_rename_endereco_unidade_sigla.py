# Generated by Django 5.0.2 on 2025-05-27 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_delete_configuracaosite_delete_contato_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unidade',
            old_name='endereco',
            new_name='sigla',
        ),
    ]
