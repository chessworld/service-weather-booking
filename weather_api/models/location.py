from django.db import models
import logging

from ..weather_providers import bom


class LocationManager(models.Manager):
    def get(self, *args, **kwargs):
        try:
            return super().get(*args, **kwargs)
        except Location.DoesNotExist:
            logging.info('SEARCHING FOR POSTCODE')
            location_data = bom.search_location(search=kwargs.get('postcode'))

            for location in location_data:
                if location['name'].lower() == kwargs.get('suburb').lower() and location['state'].lower() == kwargs.get('state').lower() and kwargs.get('country').lower() == 'Australia'.lower():
                    new_location = {
                        "suburb": location['name'],
                        "state": location['state'],
                        "postcode": location['postcode'],
                        "country": "Australia"
                    }
                    logging.info(f'New location created {new_location}')
                    return self.create(**new_location)
            raise


class Location(models.Model):
    objects = LocationManager()

    suburb   = models.CharField(max_length=100)
    state    = models.CharField(max_length=3)
    postcode = models.CharField(max_length=4)
    country  = models.CharField(max_length=100)
