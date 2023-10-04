from django.test import TestCase
from django.urls import reverse
import json
from rest_framework import status

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

    def test_patch_user(self):
        user = User.objects.create()
        url = reverse('user_detail', args=[user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], str(user.id))

        url = reverse('user_detail', args=[user.id])
        payload = {
            'name': 'Updated User',
            'completed_tutorial': True
        }
        response = self.client.patch(url, data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user.refresh_from_db()
        self.assertEqual((response.data['id']), str(user.id))
        self.assertEqual(response.data['name'], 'Updated User')
        self.assertEqual(response.data['completed_tutorial'], True)

    def test_patch_user_invalid(self):
        user = User.objects.create()
        url = reverse('user_detail', args=[user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], str(user.id))

        url = reverse('user_detail', args=[user.id])
        payload = {
            'name': 'Updated User',
            'completed_tutorial': 'Invalid Text',
        }
        response = self.client.patch(url, data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
