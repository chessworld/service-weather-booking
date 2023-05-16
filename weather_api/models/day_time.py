from django.db import models


class DayTime(models.Model):
    TIME_PERIOD_CHOICES = [
        ('Morning', 'Morning'),
        ('Afternoon', 'Afternoon'),
        ('Evening', 'Evening'),
        ('Night', 'Night'),
    ]
    
    
    date           = models.DateField()
    time_period    = models.CharField(max_length=25, choices=TIME_PERIOD_CHOICES)
    start_time     = models.TimeField()
    end_time       = models.TimeField()