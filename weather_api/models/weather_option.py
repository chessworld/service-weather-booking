from django.db import models


class WeatherOption(models.Model):
    WEATHER_TYPES = [
        ('Cloudy', 'Cloudy'),
        ('Sunny', 'Sunny'),
        ('Rainy', 'Rainy'),
        ('Stormy', 'Stormy'),
    ]
    weather = models.CharField(max_length=25, choices=WEATHER_TYPES)

    WIND_LEVELS = [
        ('No Wind', 'No Wind'),
        ('Calm', 'Calm'),
        ('Windy', 'Windy'),
    ]
    wind = models.CharField(max_length=25, choices=WIND_LEVELS)

    TEMERATURE_LEVELS = [
        ('Cool', 'Cool'),
        ('Warm', 'Warm'),
        ('Hot', 'Hot'),
    ]
    temperature = models.CharField(max_length=25, choices=TEMERATURE_LEVELS)
