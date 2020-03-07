# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-07 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0010_issue_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='status',
            field=models.CharField(blank=True, choices=[('Bug', 'Bug'), ('Feature', 'Feature')], max_length=30),
        ),
    ]
