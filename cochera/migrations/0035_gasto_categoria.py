# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0034_categoriagasto'),
    ]

    operations = [
        migrations.AddField(
            model_name='gasto',
            name='categoria',
            field=models.ForeignKey(blank=True, to='cochera.CategoriaGasto', null=True),
            preserve_default=True,
        ),
    ]
