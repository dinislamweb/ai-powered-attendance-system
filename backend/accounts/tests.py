from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase


class LoginApiTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="student1",
            email="student@example.com",
            password="StrongPass123",
            first_name="Jane",
            last_name="Doe",
        )

    def test_login_with_email_returns_token_and_user(self):
        response = self.client.post(
            reverse("login"),
            {
                "email": "student@example.com",
                "password": "StrongPass123",
            },
            format="json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertEqual(
            response.data["user"]["email"],
            "student@example.com",
        )
        self.assertEqual(
            response.data["user"]["role"],
            "student",
        )