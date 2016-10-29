# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-04 00:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacion_Entorno_familiar', models.TextField()),
                ('motivo_consulta', models.TextField()),
                ('antecedentes_personales', models.TextField()),
                ('alergicos', models.CharField(max_length=100)),
                ('vacuna', models.ImageField(upload_to='vacuna')),
                ('examen_fisico', models.TextField()),
                ('fc', models.IntegerField()),
                ('fr', models.IntegerField()),
                ('pc', models.IntegerField()),
                ('talla', models.FloatField()),
                ('peso', models.IntegerField()),
                ('pa', models.IntegerField()),
                ('imc', models.FloatField()),
                ('av', models.IntegerField()),
                ('cabeza_cuello', models.CharField(max_length=100)),
                ('cardio_pulmonar', models.CharField(max_length=100)),
                ('abdomen', models.CharField(max_length=100)),
                ('extremidades', models.CharField(max_length=100)),
                ('piel_anexos', models.CharField(max_length=100)),
                ('observaciones', models.TextField()),
                ('fecha_creacion', models.DateField()),
            ],
        ),
    ]
