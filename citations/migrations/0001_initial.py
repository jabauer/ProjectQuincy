# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bibliography',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('entry', models.TextField(blank=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'bibliographies',
                'verbose_name_plural': 'Bibliographies',
            },
        ),
        migrations.CreateModel(
            name='Citation',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('title', models.CharField(max_length=765, blank=True)),
                ('pages', models.CharField(max_length=765, blank=True)),
                ('canonic_url', models.CharField(max_length=765, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('bibliography', models.ForeignKey(blank=True, to='citations.Bibliography', null=True)),
            ],
            options={
                'db_table': 'citations',
            },
        ),
        migrations.CreateModel(
            name='Validation',
            fields=[
                ('id', models.AutoField(serialize=False, editable=False, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('supports', models.NullBooleanField()),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('auth_user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('citation', models.ForeignKey(blank=True, to='citations.Citation', null=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'db_table': 'validations',
            },
        ),
    ]
