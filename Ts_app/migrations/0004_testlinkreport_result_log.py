# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-19 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ts_app', '0003_blogcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='testlinkreport',
            name='result_log',
            field=models.FileField(blank=True, null=True, upload_to='log'),
        ),
    ]