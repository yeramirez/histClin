# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-28 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='rm',
            field=models.IntegerField(default='24343'),
            preserve_default=False,
        ),
    ]
