from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from ..models import User, Booking, Location, WeatherOption

class BookingCreateTest(TestCase):
    def setUp(self):
        # assuming these are the attributes for your models
        self.user = User.objects.create()
        self.location = Location.objects.create(suburb='Test Suburb', state='TS', postcode='1234', country='Test Country')
        self.weather_option = WeatherOption.objects.create(weather='Cloudy', wind='No Wind', temperature='Cool')
        self.date='2023-12-30'
        self.time_period = 'Morning'

        self.valid_payload = {
            'user': self.user.id,
            'location': self.location.id,
            'date': self.date,
            'time_period': self.time_period,
            'weather_option': {
                "weather": "Cloudy",
                "wind": "No Wind",
                "temperature": "Cool"
                },
            'status': 'Upcoming',
            'result': 'Pending'
        }

    def test_create_booking(self):
        response = self.client.post(reverse('booking_create'), self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)