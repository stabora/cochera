# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0036_remove_gasto_descripcion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoriagasto',
            options={'verbose_name': 'Categor\xeda de gasto', 'verbose_name_plural': 'Categor\xedas de gastos'},
        ),
        migrations.AlterField(
            model_name='gasto',
            name='categoria',
            field=models.ForeignKey(to='cochera.CategoriaGasto'),
        ),
    ]
