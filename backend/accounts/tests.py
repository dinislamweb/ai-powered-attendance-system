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
            {"email": "student@example.com", "password": "StrongPass123"},
            format="json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.data)
        self.assertEqual(response.data["user"]["email"], "student@example.com")
        self.assertEqual(response.data["user"]["role"], "student")


class UserManagementApiTests(APITestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create_user(
            username="admin1",
            email="admin@example.com",
            password="AdminPass123",
            is_staff=True,
            is_superuser=True,
        )

    def test_admin_can_list_and_create_users(self):
        self.client.force_authenticate(user=self.admin_user)

        list_response = self.client.get(reverse("user-list"))
        self.assertEqual(list_response.status_code, 200)

        create_response = self.client.post(
            reverse("user-list"),
            {
                "username": "teacher1",
                "email": "teacher@example.com",
                "password": "TeacherPass123",
                "first_name": "Alice",
                "last_name": "Brown",
                "role": "teacher",
            },
            format="json",
        )

        self.assertEqual(create_response.status_code, 201)
        self.assertEqual(create_response.data["user"]["email"], "teacher@example.com")
        self.assertEqual(create_response.data["user"]["role"], "teacher")
