# Generated by Django 5.0.2 on 2025-07-03 13:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_dfc_cd_nivel_dfc_cd_nivel2_dfc_nivel_dfc_nivel2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plano_contas',
            name='dfc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.dfc'),
        ),
        migrations.AlterField(
            model_name='plano_contas',
            name='dre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.dre'),
        ),
    ]
