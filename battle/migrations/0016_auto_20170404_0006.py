# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 22:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0029_worldunit_generation_size'),
        ('battle', '0015_auto_20170403_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='battlecontubernium',
            name='battle_unit',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='battle.BattleUnit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='battlecontuberniuminturn',
            name='battle_contubernium',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='battle.BattleContubernium'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='battlesoldier',
            name='battle_contubernium',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='battle.BattleContubernium'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='battlesoldier',
            name='world_npc',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='world.NPC'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='battlesoldierinturn',
            name='battle_soldier',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='battle.BattleSoldier'),
            preserve_default=False,
        ),
    ]
