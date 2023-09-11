from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class FeedbackTests(TestCase):
    def test_create_feedback(self):
        url = reverse('feedback_create')
        data = {
            'rating': 5,
            'comment': 'Great service!'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('id' in response.data)

    def test_create_invalid_feedback_rating_outside_range(self):
        url = reverse('feedback_create')
        data = {
            'rating': 10,
            'comment': 'Great service!'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_invalid_feedback_rating_float(self):
        url = reverse('feedback_create')
        data = {
            'rating': 3.5,
            'comment': 'Great service!'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)