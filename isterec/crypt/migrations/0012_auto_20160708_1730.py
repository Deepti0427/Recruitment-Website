# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 14:30
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypt', '0011_auto_20160708_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptrecdata',
            name='mobileno',
            field=models.CharField(default='+91', max_length=16, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='cryptrecdata',
            name='rollno',
            field=models.CharField(default='', max_length=15, validators=[django.core.validators.RegexValidator(message="Roll number must be entered in the format: '15XX101'.", regex='^\\d{2,8}?([a-z]{2}|[A-Z]{2})\\w{2,6}$')]),
        ),
    ]