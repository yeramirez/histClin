# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-04 00:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellidos', models.CharField(max_length=20)),
                ('mail', models.EmailField(max_length=254)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=1)),
                ('edad', models.IntegerField()),
                ('Doc', models.IntegerField(unique=True)),
                ('domicilio', models.CharField(max_length=30)),
                ('colegio', models.CharField(max_length=10)),
                ('grado', models.IntegerField()),
                ('madre', models.CharField(max_length=10)),
                ('padre', models.CharField(max_length=10)),
                ('telefono', models.IntegerField()),
                ('Medico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medico.Medico')),
            ],
        ),
    ]
