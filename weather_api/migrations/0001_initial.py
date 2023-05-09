# Generated by Django 3.2.18 on 2023-05-09 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suburb', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=3)),
                ('postcode', models.CharField(max_length=4)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
    ]
