# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20170430_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='barbaric',
            field=models.BooleanField(default=False),
        ),
    ]
