from django.db import models

class Location(models.Model):
    suburb   = models.CharField(max_length=100)
    state    = models.CharField(max_length=3)
    postcode = models.CharField(max_length=4)
    country  = models.CharField(max_length=100)
