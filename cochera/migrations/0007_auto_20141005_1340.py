# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0006_auto_20141005_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='titular',
            field=models.ForeignKey(to='cochera.Persona'),
        ),
    ]
