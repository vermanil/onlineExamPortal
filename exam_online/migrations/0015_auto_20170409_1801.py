# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-09 18:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('exam_online', '0014_timemanager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timemanager',
            name='startTime',
            field=models.TimeField(default=datetime.datetime(2017, 4, 9, 18, 1, 1, 436329, tzinfo=utc)),
        ),
    ]
