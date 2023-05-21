from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from ..serializers import UserSerializer
from ..models import User

class UserTests(TestCase):
    def test_create_user(self):
        url = reverse('user_create')
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('id' in response.data)

    def test_get_user(self):
        user = User.objects.create()
        url = reverse('user_detail', args=[user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], str(user.id))