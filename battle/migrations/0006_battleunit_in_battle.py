# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-14 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0005_auto_20170504_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='battleunit',
            name='in_battle',
            field=models.BooleanField(default=True),
        ),
    ]