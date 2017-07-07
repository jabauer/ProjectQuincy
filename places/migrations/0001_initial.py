# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=765, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'continents',
            },
        ),
        migrations.CreateModel(
            name='CoordinateSystem',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('short_name', models.CharField(max_length=150, blank=True)),
                ('long_name', models.CharField(max_length=765, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('reference', models.CharField(max_length=765, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'coordinate_systems',
            },
        ),
        migrations.CreateModel(
            name='Empire',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=765, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'empires',
            },
        ),
        migrations.CreateModel(
            name='InEmpire',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('start_year', models.IntegerField(null=True, blank=True)),
                ('end_year', models.IntegerField(null=True, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('empire', models.ForeignKey(blank=True, to='places.Empire', null=True)),
            ],
            options={
                'db_table': 'in_empires',
            },
        ),
        migrations.CreateModel(
            name='InRegion',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'in_regions',
            },
        ),
        migrations.CreateModel(
            name='InState',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('start_year', models.IntegerField(null=True, blank=True)),
                ('end_year', models.IntegerField(null=True, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'in_states',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=765, blank=True)),
                ('lat', models.FloatField(null=True, blank=True)),
                ('long', models.FloatField(null=True, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('coordinate_system', models.ForeignKey(blank=True, to='places.CoordinateSystem', null=True)),
            ],
            options={
                'db_table': 'locations',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=765, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'regions',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=765, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('continent', models.ForeignKey(to='places.Continent')),
            ],
            options={
                'db_table': 'states',
            },
        ),
        migrations.AddField(
            model_name='instate',
            name='location',
            field=models.ForeignKey(blank=True, to='places.Location', null=True),
        ),
        migrations.AddField(
            model_name='instate',
            name='state',
            field=models.ForeignKey(blank=True, to='places.State', null=True),
        ),
        migrations.AddField(
            model_name='inregion',
            name='location',
            field=models.ForeignKey(blank=True, to='places.Location', null=True),
        ),
        migrations.AddField(
            model_name='inregion',
            name='region',
            field=models.ForeignKey(blank=True, to='places.Region', null=True),
        ),
        migrations.AddField(
            model_name='inempire',
            name='state',
            field=models.ForeignKey(blank=True, to='places.State', null=True),
        ),
    ]
