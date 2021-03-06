# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-01 01:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180801_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cunauser',
            name='banco',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='users.Banco'),
        ),
        migrations.AlterField(
            model_name='cunauser',
            name='cuenta',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='cunauser',
            name='nombre',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
