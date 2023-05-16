from django.db import models

from .booking import Booking
from .weather_option import WeatherOption


class BookingOption(models.Model):
    booking             = models.ManyToManyField(Booking)
    weather_option      = models.ManyToManyField(WeatherOption)