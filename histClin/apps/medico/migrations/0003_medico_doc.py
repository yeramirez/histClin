# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-28 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0002_medico_rm'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='Doc',
            field=models.IntegerField(default='1046443113'),
            preserve_default=False,
        ),
    ]
