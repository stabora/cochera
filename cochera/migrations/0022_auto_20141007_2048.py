# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0021_auto_20141007_1614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacto',
            old_name='persona',
            new_name='titular',
        ),
        migrations.RenameField(
            model_name='vehiculo',
            old_name='persona',
            new_name='titular',
        ),
        migrations.AlterField(
            model_name='lugar',
            name='titular',
            field=models.ForeignKey(verbose_name=b'Titular', blank=True, to='cochera.Persona', null=True),
        ),
    ]
