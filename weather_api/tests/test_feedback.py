from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from ..models import Feedback


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