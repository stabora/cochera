# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0031_gasto'),
    ]

    operations = [
        migrations.AddField(
            model_name='lugar',
            name='comentario',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lugar',
            name='parcial',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
