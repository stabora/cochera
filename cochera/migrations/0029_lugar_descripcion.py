# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0028_auto_20141008_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='lugar',
            name='descripcion',
            field=models.CharField(default='', max_length=200, verbose_name=b'Descripci\xc3\xb3n'),
            preserve_default=False,
        ),
    ]
