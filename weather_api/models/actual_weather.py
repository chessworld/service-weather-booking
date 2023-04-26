from django.db import models

from .location import Location


class ActualWeather(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    datetime = models.DateTimeField()


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['datetime', 'location'], name='actualweather_unique_datetime_location'),
        ]
