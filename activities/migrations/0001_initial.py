# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '__first__'),
        ('people', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('start_year', models.IntegerField(null=True, blank=True)),
                ('start_certain', models.NullBooleanField()),
                ('end_year', models.IntegerField(null=True, blank=True)),
                ('end_certain', models.NullBooleanField()),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'assignments',
            },
        ),
        migrations.CreateModel(
            name='AssignmentTitle',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=765, blank=True)),
                ('temporary', models.NullBooleanField()),
                ('commissioned', models.NullBooleanField()),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'assignment_titles',
            },
        ),
        migrations.CreateModel(
            name='AssignmentType',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=765, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'assignment_types',
            },
        ),
        migrations.CreateModel(
            name='Member',
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
                'db_table': 'members',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=765, blank=True)),
                ('start_year', models.IntegerField(null=True, blank=True)),
                ('end_year', models.IntegerField(null=True, blank=True)),
                ('magazine_sending', models.NullBooleanField()),
                ('org_bio', models.TextField(blank=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('location', models.ForeignKey(on_delete=models.PROTECT, blank=True, to='places.Location', null=True)),
            ],
            options={
                'db_table': 'organizations',
            },
        ),
        migrations.CreateModel(
            name='OrganizationType',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=765, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'organization_types',
            },
        ),
        migrations.CreateModel(
            name='OrgEvolution',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('day_known', models.NullBooleanField()),
                ('month_known', models.NullBooleanField()),
                ('year_known', models.NullBooleanField()),
                ('org_1', models.ForeignKey(on_delete=models.PROTECT, related_name='org_1', blank=True, to='activities.Organization', null=True)),
                ('org_2', models.ForeignKey(on_delete=models.PROTECT, related_name='org_2', blank=True, to='activities.Organization', null=True)),
            ],
            options={
                'db_table': 'org_evolutions',
            },
        ),
        migrations.CreateModel(
            name='OrgEvolutionType',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=765, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'org_evolution_types',
            },
        ),
        migrations.CreateModel(
            name='RoleTitle',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=765, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'role_titles',
            },
        ),
        migrations.CreateModel(
            name='RoleType',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=765, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'role_types',
            },
        ),
        migrations.AddField(
            model_name='roletitle',
            name='role_type',
            field=models.ForeignKey(on_delete=models.PROTECT, blank=True, to='activities.RoleType', null=True),
        ),
        migrations.AddField(
            model_name='orgevolution',
            name='org_evolution_type',
            field=models.ForeignKey(on_delete=models.PROTECT, blank=True, to='activities.OrgEvolutionType', null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='organization_type',
            field=models.ForeignKey(on_delete=models.PROTECT, blank=True, to='activities.OrganizationType', null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='organization',
            field=models.ForeignKey(on_delete=models.PROTECT, blank=True, to='activities.Organization', null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='role_title',
            field=models.ForeignKey(on_delete=models.PROTECT, blank=True, to='activities.RoleTitle', null=True),
        ),
        migrations.AddField(
            model_name='assignmenttitle',
            name='assignment_type',
            field=models.ForeignKey(on_delete=models.PROTECT, blank=True, to='activities.AssignmentType', null=True),
        ),
        migrations.AddField(
            model_name='assignment',
            name='assignment_title',
            field=models.ForeignKey(on_delete=models.PROTECT, blank=True, to='activities.AssignmentTitle', null=True),
        ),
        migrations.AddField(
            model_name='assignment',
            name='individual',
            field=models.ForeignKey(on_delete=models.PROTECT, blank=True, to='people.Individual', null=True),
        ),
        migrations.AddField(
            model_name='assignment',
            name='location',
            field=models.ForeignKey(on_delete=models.PROTECT, blank=True, to='places.Location', null=True),
        ),
    ]
