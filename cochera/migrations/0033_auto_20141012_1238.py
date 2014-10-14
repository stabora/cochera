# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0032_auto_20141012_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lugar',
            name='comentario',
        ),
        migrations.RemoveField(
            model_name='lugar',
            name='parcial',
        ),
        migrations.AddField(
            model_name='pago',
            name='comentario',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pago',
            name='parcial',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
