from django.db import models
import uuid

from .day_time import DayTime
from .location import Location
from .user import User
from .weather_option import WeatherOption


class Booking(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    location    = models.ForeignKey(Location, on_delete=models.CASCADE)
    day_time    = models.ForeignKey(DayTime, on_delete=models.CASCADE)
    weather_option = models.ForeignKey(WeatherOption, on_delete=models.CASCADE)

    BOOKING_STATUS_CHOICES = [
        ('Upcoming', 'Upcoming'),
        ('Completed', 'Completed')
    ]
    status      = models.CharField(max_length=100, choices=BOOKING_STATUS_CHOICES, default='Upcoming')

    BOOKING_RESULT_CHOICES = [
        ('Successful', 'Successful'),
        ('Failed', 'Failed'),
        ('Pending', 'Pending')
    ]
    result      = models.CharField(max_length=100, choices=BOOKING_RESULT_CHOICES, default='Pending')
