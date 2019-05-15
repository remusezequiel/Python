# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-05-15 01:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('legajo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('appelidos', models.CharField(max_length=25)),
                ('edad', models.IntegerField()),
                ('telefono', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('direccion_domiciolio', models.TextField()),
            ],
        ),
    ]
