# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=765, blank=True)),
                ('sex', models.CharField(max_length=765, blank=True)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('death_date', models.DateField(null=True, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('sort_name', models.CharField(max_length=765, blank=True)),
                ('american', models.NullBooleanField()),
                ('birth_day_known', models.NullBooleanField()),
                ('birth_month_known', models.NullBooleanField()),
                ('birth_year_known', models.NullBooleanField()),
                ('death_day_known', models.NullBooleanField()),
                ('death_month_known', models.NullBooleanField()),
                ('death_year_known', models.NullBooleanField()),
                ('state', models.ForeignKey(on_delete=models.PROTECT, blank=True, to='places.State', null=True)),
            ],
            options={
                'db_table': 'individuals',
            },
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('start_year', models.IntegerField(null=True, blank=True)),
                ('end_year', models.IntegerField(null=True, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('individual', models.ForeignKey(on_delete=models.PROTECT, blank=True, to='people.Individual', null=True)),
            ],
            options={
                'db_table': 'occupations',
            },
        ),
        migrations.CreateModel(
            name='OccupationTitle',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=765, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'occupation_titles',
            },
        ),
        migrations.CreateModel(
            name='OccupationType',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=765, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'occupation_types',
            },
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('start_year', models.IntegerField(null=True, blank=True)),
                ('end_year', models.IntegerField(null=True, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('individual_id_1', models.ForeignKey(on_delete=models.PROTECT, related_name='individual_1', db_column=b'individual_id_1', blank=True, to='people.Individual', null=True)),
                ('individual_id_2', models.ForeignKey(on_delete=models.PROTECT, related_name='individual_2', db_column=b'individual_id_2', blank=True, to='people.Individual', null=True)),
            ],
            options={
                'db_table': 'relationships',
            },
        ),
        migrations.CreateModel(
            name='RelationshipType',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=765, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'relationship_types',
            },
        ),
        migrations.CreateModel(
            name='Residence',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('start_year', models.IntegerField(null=True, blank=True)),
                ('end_year', models.IntegerField(null=True, blank=True)),
                ('birth_place', models.NullBooleanField()),
                ('death_place', models.NullBooleanField()),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('individual', models.ForeignKey(on_delete=models.PROTECT, blank=True, to='people.Individual', null=True)),
                ('location', models.ForeignKey(on_delete=models.PROTECT, blank=True, to='places.Location', null=True)),
            ],
            options={
                'db_table': 'residences',
            },
        ),
        migrations.CreateModel(
            name='ResidenceType',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=765, blank=True)),
                ('temporary', models.NullBooleanField()),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'residence_types',
            },
        ),
        migrations.AddField(
            model_name='residence',
            name='residence_type',
            field=models.ForeignKey(on_delete=models.PROTECT, blank=True, to='people.ResidenceType', null=True),
        ),
        migrations.AddField(
            model_name='relationship',
            name='relationship_type',
            field=models.ForeignKey(on_delete=models.PROTECT, blank=True, to='people.RelationshipType', null=True),
        ),
        migrations.AddField(
            model_name='occupationtitle',
            name='occupation_type',
            field=models.ForeignKey(on_delete=models.PROTECT, blank=True, to='people.OccupationType', null=True),
        ),
        migrations.AddField(
            model_name='occupation',
            name='occupation_title',
            field=models.ForeignKey(on_delete=models.PROTECT, blank=True, to='people.OccupationTitle', null=True),
        ),
    ]
