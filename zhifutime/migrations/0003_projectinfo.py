# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 06:35
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('zhifutime', '0002_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', tinymce.models.HTMLField()),
            ],
        ),
    ]
