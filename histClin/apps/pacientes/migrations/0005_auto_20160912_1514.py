# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-12 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0004_auto_20160912_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='talla',
            field=models.DecimalField(decimal_places=3, max_digits=3),
        ),
    ]
