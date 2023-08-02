from django.db import models

from .location import Location



class ActualWeather(models.Model):
    location        = models.ForeignKey(Location, on_delete=models.CASCADE)
    date            = models.DateField()
    
    TIME_PERIOD_CHOICES = [
        ('Morning', 'Morning'),
        ('Afternoon', 'Afternoon'),
        ('Evening', 'Evening'),
        ('Night', 'Night'),
    ]
    time_period    = models.CharField(max_length=25, choices=TIME_PERIOD_CHOICES)


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['date', 'time_period', 'location'], name='actualweather_unique_datetime_location'),
        ]