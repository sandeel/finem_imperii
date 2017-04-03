# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 21:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0013_auto_20170403_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='BattleCharacterInTurn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('battle_character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='battle.BattleCharacter')),
            ],
        ),
        migrations.CreateModel(
            name='BattleContubernium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BattleContuberniumInTurn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BattleNPC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BattleNPCInTurn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BattleOrganizationInTurn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('battle_organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='battle.BattleOrganization')),
                ('battle_turn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='battle.BattleTurn')),
            ],
        ),
        migrations.AddField(
            model_name='battlecharacterinturn',
            name='battle_organization_in_turn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='battle.BattleOrganizationInTurn'),
        ),
        migrations.AddField(
            model_name='battlecharacterinturn',
            name='battle_turn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='battle.BattleTurn'),
        ),
    ]
