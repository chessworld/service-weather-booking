from django.db import models
import uuid

from .location import Location
from .user import User
from .weather_option import WeatherOption
from ..enums import TIME_PERIOD_CHOICES, BOOKING_STATUS_CHOICES, BOOKING_RESULT_CHOICES


class Booking(models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    location        = models.ForeignKey(Location, on_delete=models.CASCADE)
    weather_option  = models.ForeignKey(WeatherOption, on_delete=models.CASCADE)
    date            = models.DateField()
    time_period     = models.CharField(max_length=25, choices=TIME_PERIOD_CHOICES)
    status          = models.CharField(max_length=100, choices=BOOKING_STATUS_CHOICES, default='Upcoming')
    result          = models.CharField(max_length=100, choices=BOOKING_RESULT_CHOICES, default='Pending')
