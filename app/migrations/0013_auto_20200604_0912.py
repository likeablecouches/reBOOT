# Generated by Django 2.2.10 on 2020-06-04 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_donation_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='donor',
            options={'default_permissions': (
                'add', 'change', 'delete', 'view', 'destroy')},
        ),
        migrations.AlterModelOptions(
            name='donation',
            options={'default_permissions': (
                'add', 'change', 'delete', 'view', 'destroy')},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'default_permissions': (
                'add', 'change', 'delete', 'view', 'destroy')},
        ),
    ]
