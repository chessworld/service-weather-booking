from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from ..models import Location


class LocationSearchTests(TestCase):
    def setUp(self):
        Location.objects.create(suburb='Test Suburb', state='TS', postcode='1234', country='Test Country')

    def test_search_location(self):
        url = reverse('location_search')
        response = self.client.get(url, {'query': 'Test'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)