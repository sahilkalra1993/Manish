# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-16 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170616_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='wish_text',
            field=models.CharField(max_length=75),
        ),
    ]
