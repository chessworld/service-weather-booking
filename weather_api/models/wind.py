from django.db import models


class Wind(models.Model):
    WIND_CHOICES = [
        ('No Wind', 'No Wind'),
        ('Calm', 'Calm'),
        ('Windy', 'Windy'),
        ('Gusty', 'Gusty'),
    ]
    wind = models.CharField(max_length=25, choices=WIND_CHOICES)
