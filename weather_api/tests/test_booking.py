from django.test import TestCase
from django.urls import reverse
import json
from rest_framework import status

from ..models import User, Location, WeatherOption


class BookingCreateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create()
        self.location = Location.objects.create(suburb='Test Suburb', state='TS', postcode='1234', country='Test Country')
        self.weather_option = WeatherOption.objects.create(weather='Cloudy', wind='No Wind', temperature='Cool')
        self.date='2023-12-30'
        self.time_period = 'Morning'

    def test_create_booking(self):
        payload = {
            'user': str(self.user.id),
            'location': self.location.id,
            'date': self.date,
            'time_period': self.time_period,
            'weather_option': {
                'weather': 'Cloudy',
                'wind': 'No Wind',
                'temperature': 'Cool'
            },
            'status': 'Upcoming',
            'result': 'Pending'
        }
        response = self.client.post(reverse('booking_create'), data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_booking(self):
        payload = {
            'user': str(self.user.id),
            'location': self.location.id,
            'date': self.date,
            'time_period': self.time_period,
            'weather_option': {
                'weather': 'Invalid',
                'wind': 'No Wind',
                'temperature': 'Cool'
            }
        }
        response = self.client.post(reverse('booking_create'), data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
