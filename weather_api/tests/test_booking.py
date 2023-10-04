from django.test import TestCase
from django.urls import reverse
import json
from rest_framework import status

from ..models import User, Location, WeatherOption, Booking


class BookingCreateTest(TestCase):
    def setUp(self):
        self.user           = User.objects.create()
        self.booking_name   = 'Booking Test'
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
            'booking_name': self.booking_name,
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


    def _create_booking(self, user=None):
        if not user:
            user = self.user

        payload = {
            'user_id' : user.id,
            'booking_name': self.booking_name,
            'date': self.date,
            'time_period': self.time_period,
            'status': self.status,
            'result': self.result
        }
        booking = Booking.objects.create(location=self.location, weather_option=self.weather_option, **payload)
        return booking


    def test_get_booking(self):
        booking: Booking = self._create_booking()
        url = reverse('booking_get_patch_resource', args=[booking.id])
        response = self.client.get(url, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(str(booking.id), response.data['id'])


    def test_get_user_bookings(self):
        user = User.objects.create()
        booking: Booking = self._create_booking(user=user)
        url = reverse('booking_get_post_resource', args=[user.id])
        response = self.client.get(url, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(str(booking.id), response.data[0]['id'])


    def test_create_booking_new_location(self):
        payload = {
            'booking_name': self.booking_name,
            'location': {
                'suburb':'Melbourne',
                'state':'VIC',
                'postcode':'3000',
                'country':'Australia'
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
        self.client.post(url, data=json.dumps(payload), content_type='application/json')
        location = Location.objects.filter(
            suburb = payload['location']['suburb'],
            state = payload['location']['state'],
            postcode = payload['location']['postcode'],
            country = "Australia"
        )
        self.assertNotEqual(location, None)

    def test_create_invalid_booking(self):
        payload = {
            'booking_name': self.booking_name,
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
        url = reverse('booking_get_patch_resource', args=[booking.id])
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
        url = reverse('booking_get_patch_resource', args=[booking.id])
        response = self.client.patch(url, data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
