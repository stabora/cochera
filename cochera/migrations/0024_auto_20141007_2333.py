# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0023_auto_20141007_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='titular',
            field=models.ForeignKey(to='cochera.Titular'),
        ),
    ]
