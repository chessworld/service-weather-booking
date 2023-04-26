from django.db import models

from .wind import Wind
from .temperature import Temperature
from .weather_option import WeatherOption


class Weather(models.Model):
    wind           = models.ForeignKey(Wind, on_delete=models.CASCADE)
    temperature    = models.ForeignKey(Temperature, on_delete=models.CASCADE)
    weather_option = models.ForeignKey(WeatherOption, on_delete=models.CASCADE)
