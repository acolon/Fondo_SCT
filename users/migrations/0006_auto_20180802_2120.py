# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-02 21:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20180801_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cunauser',
            name='miembro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to='miembros.Miembro'),
        ),
    ]
