from django.db import models

from .location import Location
from .day_time import DayTime


class WeatherOption(models.Model):
    WEATHER_OPTION_TYPES = [
        ('Weather', 'Weather'),
        ('Temperature', 'Temperature'),
        ('Wind', 'Wind')
    ]
    option_type     = models.CharField(max_length=25, choices=WEATHER_OPTION_TYPES)


    WEATHER_OPTION_CHOICES = [
        ('Sunny', 'Sunny'),
        ('Rainy', 'Rainy'),
        ('Cloudy', 'Cloudy'),
        ('Stormy', 'Stormy'),
        ('Cool', 'Cool'),
        ('Mild', 'Mild'),
        ('Warm', 'Warm'),
        ('Hot', 'Hot'),
        ('Freezing', 'Freezing'),
        ('No Wind', 'No Wind'),
        ('Calm', 'Calm'),
        ('Windy', 'Windy'),
        ('Gusty', 'Gusty'),
    ]
    option_name     = models.CharField(max_length=25, choices=WEATHER_OPTION_CHOICES)


    WEATHER_VALUE_TYPE = [
        ('Km/h', 'Km/h'),
        ('Celsius', 'Celsius'),
    ]
    value_type      = models.CharField(max_length=25, choices=WEATHER_VALUE_TYPE)


    min_value       = models.IntegerField()
    max_value       = models.IntegerField()
    location        = models.ForeignKey(Location, on_delete=models.CASCADE)
    day_time        = models.ForeignKey(DayTime, on_delete=models.CASCADE)