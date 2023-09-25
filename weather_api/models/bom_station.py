from django.db import models
import logging

from location import Location
from ..services import bom


class BomStation(models.Model):
    station_name    = models.CharField(max_length=100)
    wmo_id          = models.CharField(max_length=10)
    product_id      = models.CharField(max_length=20)


class BomLocation(models.Model):
    location        = models.ForeignKey(Location, on_delete=models.CASCADE)
    station         = models.ForeignKey(BomStation, on_delete=models.CASCADE)
    geohash         = models.CharField(max_length=6)
    lattitude       = models.FloatField()
    longitude       = models.FloatField()
