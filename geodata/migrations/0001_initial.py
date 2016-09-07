# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-07 07:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('geotype', models.IntegerField(choices=[(0, b''), (1, 'District / Neighborhood'), (2, 'Town / City'), (3, 'Valley / Region'), (4, 'Province'), (5, 'State'), (6, 'Country')], db_index=True, default=0)),
                ('notes', models.TextField(blank=True, null=True)),
                ('lat', models.FloatField(default=0)),
                ('lon', models.FloatField(default=0)),
                ('added', models.DateField(auto_now_add=True, verbose_name='Added')),
                ('modified', models.DateField(auto_now=True, verbose_name='Modified')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child_set', to='geodata.Place')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Place',
                'verbose_name_plural': 'Places',
            },
        ),
        migrations.CreateModel(
            name='Polygon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limits', models.TextField(blank=True, null=True)),
                ('is_visible', models.BooleanField(default=1)),
                ('is_exterior', models.BooleanField(default=1)),
                ('encode_points', models.TextField(blank=True, null=True)),
                ('encode_levels', models.TextField(blank=True, null=True)),
                ('encode_zoomfactor', models.CharField(blank=True, max_length=20, null=True)),
                ('encode_numlevels', models.CharField(blank=True, max_length=20, null=True)),
                ('added', models.DateField(auto_now_add=True, verbose_name='Added')),
                ('modified', models.DateField(auto_now=True, verbose_name='Modified')),
                ('tokia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geodata.Place')),
            ],
            options={
                'verbose_name': 'Polygon',
                'verbose_name_plural': 'Polygons',
            },
        ),
    ]
