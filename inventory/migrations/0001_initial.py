# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-05 01:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reagent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reagent_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='antibody_reagent',
            fields=[
                ('reagent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='inventory.reagent')),
                ('analyte', models.CharField(max_length=20)),
                ('fluor', models.CharField(max_length=20)),
                ('manufacturer', models.CharField(max_length=25)),
                ('item_number', models.CharField(max_length=25)),
                ('manu_volume', models.IntegerField(default=0)),
                ('volume_per_test', models.IntegerField(default=0)),
                ('volume_per_vial', models.IntegerField(default=0)),
                ('tests_per_vial', models.IntegerField(default=0)),
                ('concentration', models.IntegerField(default=0)),
                ('isotype', models.CharField(max_length=20)),
                ('light_chain', models.CharField(max_length=20)),
                ('clone', models.CharField(max_length=20)),
                ('control_cells', models.CharField(max_length=750)),
            ],
        ),
    ]
