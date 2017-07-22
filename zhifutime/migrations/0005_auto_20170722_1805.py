# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 08:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('zhifutime', '0004_auto_20170722_1723'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-publish',)},
        ),
        migrations.AddField(
            model_name='article',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2017, 7, 22, 8, 5, 49, 333827, tzinfo=utc), max_length=250, unique_for_date='publish'),
            preserve_default=False,
        ),
    ]