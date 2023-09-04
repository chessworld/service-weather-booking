from django.test import TestCase
from django.urls import reverse
import json
from rest_framework import status

from ..models import User, Location, WeatherOption, Booking


class BookingCreateTest(TestCase):
    def setUp(self):
        self.user           = User.objects.create()
        self.location       = Location.objects.create(suburb='Test Suburb', state='TS', postcode='1234', country='Test Country')
        self.weather_option = WeatherOption.objects.create(weather='Cloudy', wind='No Wind', temperature='Cool')
        self.date           = '2023-12-30'
        self.date_patch     = '2024-12-30'
        self.time_period    = 'Morning'
        self.result         = 'Successful'
        self.status         = 'Upcoming'
        self.result         = 'Pending'

    def test_create_booking(self):
        payload = {
            'location': {
                'suburb':'Test Suburb',
                'state':'TS',
                'postcode':'1234',
                'country':'Test Country'
            },
            'date': self.date,
            'time_period': self.time_period,
            'weather_option': {
                'weather': 'Cloudy',
                'wind': 'No Wind',
                'temperature': 'Cool'
            },
            'status': self.status,
            'result': self.result
        }
        url = reverse('booking_get_post_resource', args=[self.user.id])
        response = self.client.post(url, data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_booking(self):
        payload = {
            'location': {
                'suburb':'Test Suburb',
                'state':'TS',
                'postcode':'1234',
                'country':'Test Country'
            },
            'date': self.date,
            'time_period': self.time_period,
            'weather_option': str(self.weather_option)
        }
        url = reverse('booking_get_post_resource', args=[str(self.user.id)])
        response = self.client.post(url, data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_patch_booking(self):
        booking = Booking.objects.create(
            user=self.user,
            location=self.location,
            date=self.date,
            time_period=self.time_period,
            weather_option=self.weather_option
        )

        payload = {
            'date': self.date_patch,
            'result': self.result,
            'weather_option': {
                'weather': 'Cloudy',
                'wind': 'Windy',
                'temperature': 'Hot'
            },
        }
        url = reverse('booking_get_patch_resouce', args=[booking.id])
        response = self.client.patch(url, data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_invalid_booking(self):
        booking = Booking.objects.create(
            user=self.user,
            location=self.location,
            date=self.date,
            time_period=self.time_period,
            weather_option=self.weather_option
        )

        payload = {
            'date': self.date_patch,
            'result': ''
        }
        url = reverse('booking_get_patch_resouce', args=[booking.id])
        response = self.client.patch(url, data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
