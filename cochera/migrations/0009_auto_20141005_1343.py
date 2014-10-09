# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0008_auto_20141005_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='fecha_ocupado',
            field=models.DateField(null=True, blank=True),
        ),
    ]
