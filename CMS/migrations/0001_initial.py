# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-25 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileInfo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('userId', models.CharField(max_length=100)),
                ('addTime', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=100)),
                ('userUrl', models.URLField()),
                ('userAvaUrl', models.URLField()),
            ],
        ),
    ]
