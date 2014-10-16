# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0039_auto_20141014_2054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lugar',
            options={'ordering': ['numero'], 'verbose_name_plural': 'Lugares'},
        ),
    ]
