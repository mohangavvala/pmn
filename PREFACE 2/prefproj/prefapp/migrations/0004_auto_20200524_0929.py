# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-24 03:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prefapp', '0003_auto_20200523_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='msg',
            field=models.TextField(blank=True, null=True),
        ),
    ]