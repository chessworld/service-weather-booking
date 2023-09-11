# Generated by Django 4.2.1 on 2023-09-11 06:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_api', '0002_alter_weatheroption_weather'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='Rating must be at least 1'), django.core.validators.MaxValueValidator(5, message='Rating must be at most 5')]),
        ),
    ]
