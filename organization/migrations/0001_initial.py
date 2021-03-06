# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 18:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('ban', 'ban'), ('policy', 'write policy and law'), ('diplomacy', 'conduct diplomacy'), ('conscript', 'conscript troops'), ('dissolve', 'dissolve'), ('suborganizations', 'manage subordinate organizations'), ('secede', 'secede'), ('memberships', 'manage memberships'), ('heir', 'set heir'), ('elect', 'elect'), ('candidacy', 'present candidacy'), ('convoke elections', 'convoke elections'), ('military stance', 'military orders'), ('battle formation', 'battle formation'), ('occupy region', 'occupy region')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CapabilityProposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposal_json', models.TextField()),
                ('vote_end_turn', models.IntegerField()),
                ('executed', models.BooleanField(default=False)),
                ('closed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CapabilityVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.CharField(choices=[('yea', 'yea'), ('nay', 'nay'), ('invalid', 'invalid')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MilitaryStance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stance_type', models.CharField(choices=[('default', 'automatic by diplomatic relationship'), ('avoid battle', 'avoid battle'), ('defensive', 'defensive'), ('aggressive', 'aggressive')], default='default', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(default='FFFFFF', help_text='Format: RRGGBB (hex)', max_length=6)),
                ('description', models.TextField()),
                ('is_position', models.BooleanField()),
                ('position_type', models.CharField(blank=True, choices=[('inherited', 'inherited'), ('elected', 'elected')], default='', max_length=15)),
                ('owner_and_leader_locked', models.BooleanField(help_text="If set, this organization will have always the same leader as it's owner.")),
                ('violence_monopoly', models.BooleanField(default=False)),
                ('decision_taking', models.CharField(choices=[('democratic', 'democratic'), ('distributed', 'distributed')], max_length=15)),
                ('membership_type', models.CharField(choices=[('character', 'character'), ('organization', 'organization')], max_length=15)),
                ('election_period_months', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationship', models.CharField(choices=[('peace', 'peace'), ('war', 'war'), ('banned', 'banned'), ('friendship', 'friendship'), ('defensive alliance', 'defensive alliance'), ('alliance', 'alliance')], default='peace', max_length=20)),
                ('desired_relationship', models.CharField(blank=True, choices=[('peace', 'peace'), ('war', 'war'), ('banned', 'banned'), ('friendship', 'friendship'), ('defensive alliance', 'defensive alliance'), ('alliance', 'alliance')], max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PolicyDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public', models.BooleanField(default=False)),
                ('title', models.TextField(max_length=100)),
                ('body', models.TextField()),
                ('last_modified_turn', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PositionCandidacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('retired', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PositionElection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turn', models.IntegerField()),
                ('closed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PositionElectionVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidacy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.PositionCandidacy')),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.PositionElection')),
            ],
        ),
    ]
