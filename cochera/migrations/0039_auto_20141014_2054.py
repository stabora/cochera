# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0038_auto_20141014_2047'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='titular',
            options={'ordering': ['apellido', 'nombres'], 'verbose_name_plural': 'Titulares'},
        ),
    ]
