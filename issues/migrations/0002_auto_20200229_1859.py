# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-29 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='image',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='price',
        ),
        migrations.AddField(
            model_name='issue',
            name='expected_result',
            field=models.TextField(default='What is happening?', max_length=140),
        ),
        migrations.AddField(
            model_name='issue',
            name='steps_to_reproduce',
            field=models.TextField(default='Enter steps', max_length=140),
        ),
    ]