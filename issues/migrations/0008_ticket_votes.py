# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-19 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0007_auto_20181019_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
