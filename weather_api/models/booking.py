from django.db import models

from .user import User
from .weather import Weather
from .location import Location


class Booking(models.Model):
    user           = models.ForeignKey(User, on_delete=models.CASCADE)
    weather        = models.ForeignKey(Weather, on_delete=models.CASCADE)
    location       = models.ForeignKey(Location, on_delete=models.CASCADE)

    date           = models.DateField()

    BOOKING_STATUS_CHOICES = [
        ('Upcoming', 'Upcoming'),
        ('Completed', 'Completed')
    ]
    status          = models.CharField(max_length=100, choices=BOOKING_STATUS_CHOICES, default='Upcoming')

    result          = models.BooleanField() # Did the booking match actual weather data ?
