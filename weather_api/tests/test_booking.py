from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from ..models import User, Booking, Location, DayTime


class BookingOptionsTests(TestCase):
    def test_get_booking_options(self):
        url = reverse('booking_option_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class BookingTests(TestCase):
    def setUp(self):
        self.user = User.objects.create()
        self.location = Location.objects.create(suburb='Test Suburb', state='TS', postcode='1234', country='Test Country')
        self.day_time = DayTime.objects.create(date='2022-01-01', time_period='Morning', start_time='06:00:00', end_time='12:00:00')

    def test_create_booking(self):
        url = reverse('booking_create')
        data = {
            'user': self.user.id,
            'location': self.location.id,
            'day_time': self.day_time.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('id' in response.data)

    def test_get_booking(self):
        booking = Booking.objects.create(user=self.user, location=self.location, day_time=self.day_time)
        url = reverse('booking_detail', args=[booking.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], str(booking.id))

    # def test_update_booking(self):
    #     booking = Booking.objects.create(user=self.user, location=self.location, day_time=self.day_time)
    #     url = reverse('booking_update', args=[booking.id])
    #     data = {
    #         'status': 'Completed'
    #     }
    #     response = self.client.patch(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['status'], 'Completed')


class UserBookingsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create()
        self.location = Location.objects.create(suburb='Test Suburb', state='TS', postcode='1234', country='Test Country')
        self.day_time = DayTime.objects.create(date='2022-01-01', time_period='Morning', start_time='06:00:00', end_time='12:00:00')

    def test_get_user_bookings(self):
        Booking.objects.create(user=self.user, location=self.location, day_time=self.day_time)
        url = reverse('user_booking_list', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)