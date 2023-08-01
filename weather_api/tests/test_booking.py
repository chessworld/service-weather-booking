from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from ..models import User, Booking, Location, DayTime


class BookingOptionsTests(TestCase):
    def test_get_booking_options(self):
        url = reverse('booking_option_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserBookingsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create()
        self.location = Location.objects.create(suburb='Test Suburb', state='TS', postcode='1234', country='Test Country')
        self.day_time = DayTime.objects.create(date='2022-01-01', time_period='Morning')

    def test_get_user_bookings(self):
        Booking.objects.create(user=self.user, location=self.location, day_time=self.day_time)
        url = reverse('user_booking_list', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)