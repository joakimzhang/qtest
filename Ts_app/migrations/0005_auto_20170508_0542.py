# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-08 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ts_app', '0004_testlinkreport_result_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testlinkreport',
            name='test_result',
            field=models.CharField(choices=[('Pass', 'pass'), ('Fail', 'fail'), ('Untest', 'untest'), ('Block', 'block')], default='Untest', max_length=100),
        ),
    ]
