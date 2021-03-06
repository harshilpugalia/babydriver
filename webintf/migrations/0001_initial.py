# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-22 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('driver_uid', models.IntegerField(primary_key=True, serialize=False)),
                ('driver_mobnum', models.IntegerField(max_length=12)),
                ('driver_name', models.CharField(max_length=21)),
                ('driver_vehnum', models.IntegerField(max_length=4)),
                ('driver_operator', models.CharField(max_length=100)),
                ('driver_signup_timestamp', models.DateTimeField()),
            ],
        ),
    ]
