# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-30 04:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190130_0408'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.CharField(default='none', max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
