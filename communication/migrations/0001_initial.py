# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '__first__'),
        ('people', '__first__'),
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enclosure',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'enclosures',
            },
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('circular', models.NullBooleanField()),
                ('date_sent', models.DateField(null=True, blank=True)),
                ('date_received', models.DateField(null=True, blank=True)),
                ('date_docketed', models.DateField(null=True, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('title', models.CharField(max_length=765, blank=True)),
                ('sent_day_known', models.NullBooleanField()),
                ('sent_month_known', models.NullBooleanField()),
                ('sent_year_known', models.NullBooleanField()),
                ('received_day_known', models.NullBooleanField()),
                ('received_month_known', models.NullBooleanField()),
                ('received_year_known', models.NullBooleanField()),
                ('docketed_day_known', models.NullBooleanField()),
                ('docketed_month_known', models.NullBooleanField()),
                ('docketed_year_known', models.NullBooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('from_individual', models.ForeignKey(on_delete=models.PROTECT, related_name='individual_from', blank=True, to='people.Individual', null=True)),
                ('from_location', models.ForeignKey(on_delete=models.PROTECT, related_name='location_from', blank=True, to='places.Location', null=True)),
                ('from_organization', models.ForeignKey(on_delete=models.PROTECT, related_name='organization_from', blank=True, to='activities.Organization', null=True)),
                ('to_individual', models.ForeignKey(on_delete=models.PROTECT, related_name='individual_to', blank=True, to='people.Individual', null=True)),
                ('to_location', models.ForeignKey(on_delete=models.PROTECT, related_name='location_to', blank=True, to='places.Location', null=True)),
                ('to_organization', models.ForeignKey(on_delete=models.PROTECT, related_name='organization_to', blank=True, to='activities.Organization', null=True)),
            ],
            options={
                'db_table': 'letters',
            },
        ),
        migrations.AddField(
            model_name='enclosure',
            name='enclosed_letter',
            field=models.ForeignKey(on_delete=models.PROTECT, related_name='letter_2', blank=True, to='communication.Letter', null=True),
        ),
        migrations.AddField(
            model_name='enclosure',
            name='main_letter',
            field=models.ForeignKey(on_delete=models.PROTECT, related_name='letter_1', blank=True, to='communication.Letter', null=True),
        ),
    ]
