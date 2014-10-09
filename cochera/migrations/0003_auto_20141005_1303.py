# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0002_auto_20141005_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='fecha_ocupado',
            field=models.DateField(blank=True),
        ),
    ]
