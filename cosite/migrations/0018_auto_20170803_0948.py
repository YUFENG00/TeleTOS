# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosite', '0017_auto_20170802_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testcasestate',
            name='set_session_rate',
        ),
        migrations.AddField(
            model_name='testcasestate',
            name='set_online_rate',
            field=models.CharField(default='-1', help_text='上线速率', max_length=100),
        ),
    ]
