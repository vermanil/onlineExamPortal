# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-08 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_online', '0011_auto_20170408_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optiondetail',
            name='code',
            field=models.TextField(),
        ),
    ]
