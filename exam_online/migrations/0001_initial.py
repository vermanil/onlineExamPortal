# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-03 17:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='exam_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examCode', models.TextField()),
                ('examName', models.TextField()),
                ('totalTime', models.IntegerField()),
                ('totalMark', models.IntegerField()),
                ('createdby', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='optionDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option1', models.TextField()),
                ('option2', models.TextField()),
                ('option3', models.TextField()),
                ('option4', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='questionDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.IntegerField()),
                ('correctAnswer', models.TextField()),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_online.exam_details')),
            ],
        ),
        migrations.CreateModel(
            name='scores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('rank', models.IntegerField()),
                ('examCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_online.exam_details')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='optiondetail',
            name='q_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_online.questionDetails'),
        ),
    ]
