# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0029_lugar_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lugar',
            name='descripcion',
        ),
    ]
