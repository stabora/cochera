# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cochera', '0014_auto_20141006_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='calle',
            field=models.CharField(default=None, max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='codigo_postal',
            field=models.CharField(default=None, max_length=10, null=True, verbose_name=b'C\xc3\xb3digo postal', blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='localidad',
            field=models.CharField(default=None, max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='numero',
            field=models.IntegerField(default=None, null=True, verbose_name=b'N\xc3\xbamero', blank=True),
        ),
    ]
