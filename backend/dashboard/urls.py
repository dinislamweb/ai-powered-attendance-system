from django.urls import path
from .views import (
    AdminDashboardAPIView,
    TeacherDashboardAPIView,
    StudentDashboardAPIView,
)

urlpatterns = [
    path(
        "admin/",
        AdminDashboardAPIView.as_view(),
        name="admin-dashboard",
    ),

    path(
        "teacher/",
        TeacherDashboardAPIView.as_view(),
        name="teacher-dashboard",
    ),

    path(
        "student/",
        StudentDashboardAPIView.as_view(),
        name="student-dashboard",
    ),
]