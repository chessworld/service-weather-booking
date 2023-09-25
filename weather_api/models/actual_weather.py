from django.db import models

from .location import Location
from ..enums import TIME_PERIOD_CHOICES


class ActualWeather(models.Model):
    location        = models.ForeignKey(Location, on_delete=models.CASCADE)
    date            = models.DateField()

    time_period    = models.CharField(max_length=25, choices=TIME_PERIOD_CHOICES)


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['date', 'time_period', 'location'], name='actualweather_unique_datetime_location'),
        ]
