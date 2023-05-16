from django.db import models


class WeatherOption(models.Model):
    WEATHER_OPTION_CHOICES = [
        ('Sunny', 'Sunny'),
        ('Rainy', 'Rainy'),
        ('Cloudy', 'Cloudy'),
        ('Stormy', 'Stormy'),
    ]

    weather_option = models.CharField(max_length=25, choices=WEATHER_OPTION_CHOICES)
