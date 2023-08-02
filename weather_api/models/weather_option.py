from django.db import models

from .location import Location
from .day_time import DayTime


class WeatherOption(models.Model):
    WEATHER_TYPES = [
        ('Cloudy', 'Cloudy'),
        ('Sunny', 'Sunny'),
        ('Windy', 'Windy'),
        ('Rainy', 'Rainy'),
    ]
    weather = models.models.CharField(max_length=25, choices=WEATHER_TYPES)

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
    temperature = models.models.CharField(max_length=25, choices=TEMERATURE_LEVELS)
