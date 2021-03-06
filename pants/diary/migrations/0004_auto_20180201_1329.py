# Generated by Django 2.0.1 on 2018-02-01 02:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_diaryfood_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaryfood',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=3, help_text='g or ml for ingredients or products; number of serves for recipes', max_digits=7, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='diaryfood',
            name='cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
