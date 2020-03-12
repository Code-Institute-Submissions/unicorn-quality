# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-12 08:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0012_auto_20200310_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(default='', max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='issue',
            name='published_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='Issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='issues.Issue'),
        ),
    ]
