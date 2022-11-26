from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.status import (HTTP_200_OK, HTTP_401_UNAUTHORIZED,
                                   HTTP_403_FORBIDDEN)
from rest_framework.test import APIClient


class TestApi(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create(email="customer@example.com")
        self.user.set_password("test1234")
        self.user.save()

    def test_customer_list(self):
        self.client.force_authenticate(user=self.user)
        result = self.client.get(reverse("api:customer-list"))
        self.assertEqual(result.status_code, HTTP_200_OK)

    def test_profile_list(self):
        self.client.force_authenticate(user=self.user)
        result = self.client.get(reverse("api:profile-list"))
        self.assertEqual(result.status_code, HTTP_200_OK)

    def test_order_list(self):
        self.client.force_authenticate(user=self.user)
        result = self.client.get(reverse("api:order-list"))
        self.assertEqual(result.status_code, HTTP_200_OK)

    def test_order_list_logout(self):
        self.client.logout()
        result = self.client.get(reverse("api:order-list"))
        self.assertEqual(result.status_code, HTTP_401_UNAUTHORIZED)

    def test_vehicle_list(self):
        self.client.force_authenticate(user=self.user)
        result = self.client.get(reverse("api:vehicle-list"))
        self.assertEqual(result.status_code, HTTP_403_FORBIDDEN)

    def test_cargo_list(self):
        self.client.force_authenticate(user=self.user)
        result = self.client.get(reverse("api:cargo-list"))
        self.assertEqual(result.status_code, HTTP_403_FORBIDDEN)
