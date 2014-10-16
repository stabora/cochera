# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0040_auto_20141016_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasto',
            name='importe',
            field=models.DecimalField(max_digits=13, decimal_places=2),
        ),
    ]
