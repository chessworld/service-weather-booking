import os
import django
from django.core.wsgi import get_wsgi_application
from django.conf import settings
import logging

os.environ["DJANGO_SETTINGS_MODULE"] = 'service_weather_booking.settings'


def populate_db():
    django.setup()

    print("Populating database with initial data")
    application = get_wsgi_application()

    from weather_api.models.location import Location

    # Add dummy locations
    locations = [
        {"suburb": "Sydney", "state": "NSW", "postcode": "2000", "country": "Australia"},
        {"suburb": "Melbourne", "state": "VIC", "postcode": "3000", "country": "Australia"},
        {"suburb": "Brisbane", "state": "QLD", "postcode": "4000", "country": "Australia"},
        {"suburb": "Perth", "state": "WA", "postcode": "6000", "country": "Australia"},
        {"suburb": "Adelaide", "state": "SA", "postcode": "5000", "country": "Australia"},
    ]

    day_time = [
        {"day": "Monday", "time": "09:00"},
    ]

    for loc in locations:
        print("Adding location: {}".format(loc))
        Location.objects.create(**loc)
