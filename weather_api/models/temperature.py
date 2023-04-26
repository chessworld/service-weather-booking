from django.db import models


class Temperature(models.Model):
    TEMPERATURE_CHOICES = [
        ('Cool', 'Cool'),
        ('Mild', 'Mild'),
        ('Warm', 'Warm'),
        ('Hot', 'Hot'),
        ('Freezing', 'Freezing')
    ]

    temperature = models.CharField(max_length=25, choices=TEMPERATURE_CHOICES)
