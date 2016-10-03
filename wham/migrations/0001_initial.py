# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-03 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RateLimitingData',
            fields=[
                ('app_label', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('max_requests_per_day', models.IntegerField(null=True)),
                ('max_requests_per_minute', models.IntegerField(null=True)),
                ('day_start', models.DateField(auto_now_add=True)),
                ('minute_start', models.DateTimeField()),
                ('requests_this_day', models.IntegerField(default=0)),
                ('requests_this_minute', models.IntegerField(default=0)),
                ('max_total_requests_in_day', models.IntegerField(default=0)),
                ('max_total_requests_in_minute', models.IntegerField(default=0)),
            ],
        ),
    ]
