# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0027_parametro_nombre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parametro',
            options={'verbose_name': 'Par\xe1metro'},
        ),
        migrations.AlterField(
            model_name='parametro',
            name='descripcion',
            field=models.CharField(max_length=200, verbose_name=b'Descripci\xc3\xb3n'),
        ),
    ]
