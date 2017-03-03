# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-02 22:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_organization_members'),
        ('world', '0011_tile_controlled_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='oath_sworn_to',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='organization.Organization'),
            preserve_default=False,
        ),
    ]
