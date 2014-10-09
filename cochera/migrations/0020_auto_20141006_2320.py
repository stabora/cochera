# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0019_pago_importe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pago',
            old_name='persona',
            new_name='titular',
        ),
    ]
