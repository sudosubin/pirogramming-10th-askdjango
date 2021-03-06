# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-21 08:15
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='lnglat',
            field=models.CharField(blank=True, help_text='경도, 윈도 포맷으로 입력하세요.', max_length=50, validators=[blog.models.lnglat_validator]),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(help_text='마크다운 문법을 사용해주세요.', verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='포스팅 제목을 입력하세요. 최대 100자.', max_length=100, verbose_name='제목'),
        ),
    ]
