# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-16 20:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20180630_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='province',
            field=models.CharField(choices=[(b'AB', b'Alberta'), (b'BC', b'British Columbia'), (b'ON', b'Ontario'), (b'NS', b'Nova Scotia'), (b'NL', b'Newfoundland and Labrador'), (b'NU', b'Nunavut'), (b'YT', b'Yukon'), (b'MB', b'Manitoba'), (b'SK', b'Saskatchewan'), (b'PE', b'Prince Edward Island'), (b'NT', b'Northwest Territories'), (b'NB', b'New Brunswick'), (b'QC', b'Quebec')], max_length=20, verbose_name='Province'),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(choices=[(b'Other Printer', b'Other Printer'), (b'Camera', b'Camera'), (b'CCTV Camera', b'CCTV camera'), (b'Speaker', b'Speaker'), (b'Other Storage Device', b'Other Storage Device'), (b'Keyboard', b'Keyboard'), (b'Tablet', b'Tablet'), (b'Other gaming console', b'Gaming console'), (b'Other', b'Other'), (b'Other Network Device', b'Other Network Device'), (b'TV', b'Television'), (b'Laser Printer', b'Laser Printer'), (b'Cables', b'Cables/Connectors'), (b'LCD Monitor', b'LCD Monitor'), (b'PC-DESKTOP', b'Computer Desktop'), (b'Inkjet Printer', b'Inkjet Printer'), (b'HeatSink', b'Heat Sink'), (b'LED Monitor', b'LED Monitor'), (b'SSD', b'Solid State Drive'), (b'Xbox', b'Xbox'), (b'Fan', b'Fan'), (b'RAM', b'Ram'), (b'HDD', b'Hard Disk Drive'), (b'Router', b'Router'), (b'PSU', b'Power Supply'), (b'Webcam', b'Webcam'), (b'Floppy Drive', b'Floppy Diskette'), (b'CPU', b'CPU'), (b'Mice', b'Mice'), (b'Switch', b'Network Switch'), (b'DSLR', b'DSLR'), (b'Mobile Phone', b'Mobile Phone'), (b'PC-Laptop', b'Computer Laptop'), (b'GPU', b'Video Card'), (b'Audio Receiver', b'Audio Receiver'), (b'Playstation', b'Playstation'), (b'HeadPhone', b'Headphones'), (b'MotherBoard', b'MotherBoard'), (b'LiquidCooler', b'Liquid Cooler'), (b'AllInOne Printer', b'All-In-One Printer'), (b'Server', b'Server'), (b'Other Monitor', b'Other Monitor'), (b'3d Printer', b'3d Printer'), (b'Mic', b'Microphone')], max_length=500, verbose_name='Description'),
        ),
    ]
