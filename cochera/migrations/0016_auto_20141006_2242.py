# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0015_auto_20141006_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='descripcion',
            field=models.CharField(default=None, max_length=200, null=True, verbose_name=b'Descripci\xc3\xb3n', blank=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='dominio',
            field=models.CharField(default=None, max_length=20, null=True, blank=True),
        ),
    ]
