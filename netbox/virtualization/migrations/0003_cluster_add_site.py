# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-22 16:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0044_virtualization'),
        ('virtualization', '0002_virtualmachine_add_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='cluster',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='clusters', to='dcim.Site'),
        ),
    ]
