from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from accounts.models import Student, Teacher
from attendance.models import AttendanceSession
from batches.models import Batch
from courses.models import Course
from schedules.models import Schedule

User = get_user_model()


class DashboardAPITests(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_user(
            username="admin@example.com",
            email="admin@example.com",
            password="password123",
            first_name="Admin",
            last_name="User",
            role="admin",
        )
        self.teacher_user = User.objects.create_user(
            username="teacher@example.com",
            email="teacher@example.com",
            password="password123",
            first_name="Teacher",
            last_name="User",
            role="teacher",
        )
        self.teacher_profile = Teacher.objects.create(
            user=self.teacher_user,
            employee_id="T001",
            phone="123456789",
            designation="Instructor",
        )

        self.student_user = User.objects.create_user(
            username="student@example.com",
            email="student@example.com",
            password="password123",
            first_name="Student",
            last_name="User",
            role="student",
        )

        self.course = Course.objects.create(
            course_name="Mathematics",
            description="Core math",
            duration="8 weeks",
        )
        self.batch = Batch.objects.create(
            course=self.course,
            batch_code="B001",
            batch_name="Batch 1",
            start_date="2026-01-01",
            end_date="2026-03-01",
        )
        self.student_profile = Student.objects.create(
            user=self.student_user,
            student_id="S001",
            batch=self.batch,
            phone="987654321",
        )
        self.schedule = Schedule.objects.create(
            course=self.course,
            batch=self.batch,
            teacher=self.teacher_profile,
            day="Monday",
            start_time="09:00:00",
            end_time="10:00:00",
            room="A1",
        )
        AttendanceSession.objects.create(
            schedule=self.schedule,
            teacher=self.teacher_profile,
            date="2026-07-01",
            remarks="Test session",
        )

    def test_admin_dashboard_requires_admin_role(self):
        self.client.force_login(self.teacher_user)

        response = self.client.get(reverse("admin-dashboard"))

        self.assertEqual(response.status_code, 403)

    def test_admin_dashboard_returns_counts_for_admin_user(self):
        self.client.force_login(self.admin_user)

        response = self.client.get(reverse("admin-dashboard"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["total_students"], 1)
        self.assertEqual(response.json()["total_teachers"], 1)
        self.assertEqual(response.json()["total_courses"], 1)
        self.assertEqual(response.json()["total_batches"], 1)

    def test_teacher_dashboard_returns_teacher_metrics(self):
        self.client.force_login(self.teacher_user)

        response = self.client.get(reverse("teacher-dashboard"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["assigned_schedules"], 1)
        self.assertEqual(response.json()["total_students"], 1)
        self.assertEqual(response.json()["attendance_sessions"], 1)
        self.assertEqual(response.json()["teacher_name"], "Teacher User")
