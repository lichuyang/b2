# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0004_fileinfo_downloads'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchInfo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('searchText', models.CharField(max_length=50)),
                ('searchCount', models.IntegerField(default=0)),
            ],
        ),
    ]
