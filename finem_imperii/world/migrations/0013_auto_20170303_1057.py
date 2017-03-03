# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-03 09:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0012_character_oath_sworn_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='oath_sworn_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.Organization'),
        ),
    ]
