# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0035_gasto_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gasto',
            name='descripcion',
        ),
    ]
