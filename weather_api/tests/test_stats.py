from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class StatsTest(TestCase):
    def test_get_stats(self):
        url = reverse('stats')
        response = self.client.get(url, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
