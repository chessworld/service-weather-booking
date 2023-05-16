from django.db import models

from .location import Location
from .day_time import DayTime



class ActualWeather(models.Model):
    location        = models.ForeignKey(Location, on_delete=models.CASCADE)
    datetime        = models.ForeignKey(DayTime, on_delete=models.CASCADE)


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['datetime', 'location'], name='actualweather_unique_datetime_location'),
        ]
