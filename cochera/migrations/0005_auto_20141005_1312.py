# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0004_auto_20141005_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='fecha_ocupado',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='titular',
            field=models.ForeignKey(to='cochera.Persona'),
        ),
    ]
