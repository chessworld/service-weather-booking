# Generated by Django 4.2.1 on 2023-08-08 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weatheroption',
            name='weather',
            field=models.CharField(choices=[('Cloudy', 'Cloudy'), ('Sunny', 'Sunny'), ('Rainy', 'Rainy'), ('Stormy', 'Stormy')], max_length=25),
        ),
    ]
