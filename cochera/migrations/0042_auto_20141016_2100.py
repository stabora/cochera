# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0041_auto_20141016_1538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lugar',
            old_name='fecha_ocupado',
            new_name='fecha_ocupacion',
        ),
    ]
