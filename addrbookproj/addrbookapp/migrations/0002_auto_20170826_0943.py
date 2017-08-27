# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addrbookapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='email_id',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='phone_number',
            field=models.CharField(max_length=12, unique=True, verbose_name='number'),
        ),
    ]
