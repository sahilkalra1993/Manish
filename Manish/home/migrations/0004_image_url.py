# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-16 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20170616_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image_url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=500)),
            ],
        ),
    ]