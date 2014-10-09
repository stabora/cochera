# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0026_parametro'),
    ]

    operations = [
        migrations.AddField(
            model_name='parametro',
            name='nombre',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
