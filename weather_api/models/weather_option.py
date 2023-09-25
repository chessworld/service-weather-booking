from django.db import models

from ..enums import WEATHER_TYPES, WIND_LEVELS, TEMERATURE_LEVELS


class WeatherOption(models.Model):
    weather     = models.CharField(max_length=25, choices=WEATHER_TYPES)
    wind        = models.CharField(max_length=25, choices=WIND_LEVELS)
    temperature = models.CharField(max_length=25, choices=TEMERATURE_LEVELS)
