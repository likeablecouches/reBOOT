# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-14 10:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190805_0335'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'permissions': (('update_status_item', 'Can update item status'), (
                'update_value_item', 'Can update item value'))},
        ),
    ]
