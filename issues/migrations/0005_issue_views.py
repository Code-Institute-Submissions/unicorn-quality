# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-04 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0004_issue_issue_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
