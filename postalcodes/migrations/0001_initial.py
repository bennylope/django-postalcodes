# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostalCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=20, verbose_name='postal code')),
                ('country', models.CharField(max_length=2, verbose_name='country')),
                ('city', models.CharField(max_length=200, null=True, verbose_name='city', blank=True)),
                ('state', models.CharField(max_length=100, null=True, verbose_name='state', blank=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Postal code',
                'verbose_name_plural': 'Postal codes',
            },
        ),
    ]
