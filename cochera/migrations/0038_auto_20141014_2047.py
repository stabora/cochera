# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0037_auto_20141013_2334'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoriagasto',
            options={'ordering': ['descripcion'], 'verbose_name': 'Categor\xeda de gasto', 'verbose_name_plural': 'Categor\xedas de gastos'},
        ),
    ]
