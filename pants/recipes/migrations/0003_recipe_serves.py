# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 08:31
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20170709_0757'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='serves',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=4, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
    ]
