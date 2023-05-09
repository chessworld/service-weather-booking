import os
import django
from django.core.wsgi import get_wsgi_application
from django.conf import settings


os.environ["DJANGO_SETTINGS_MODULE"] = 'service_weather_booking.settings'
django.setup()
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

for loc in locations:
    Location.objects.create(**loc)