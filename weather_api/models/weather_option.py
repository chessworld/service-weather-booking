from django.db import models


class WeatherOption(models.Model):
    WEATHER_OPTION_CHOICES = [
        ('Spring', 'Spring'),
        ('Summer', 'Summer'),
        ('Fall', 'Fall'),
        ('Winter', 'Winter'),
    ]

    weather_option = models.CharField(max_length=25, choices=WEATHER_OPTION_CHOICES)
