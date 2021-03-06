# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-29 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_capabilityproposal_democratic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capability',
            name='type',
            field=models.CharField(choices=[('ban', 'ban'), ('policy', 'write policy and law'), ('diplomacy', 'conduct diplomacy'), ('conscript', 'conscript troops'), ('heir', 'set heir'), ('elect', 'elect'), ('candidacy', 'present candidacy'), ('convoke elections', 'convoke elections'), ('military stance', 'military orders'), ('battle formation', 'battle formation'), ('occupy region', 'occupy region'), ('take grain', 'take grain'), ('manage guilds', 'manage guilds'), ('manage taxation', 'manage taxation')], max_length=20),
        ),
    ]
