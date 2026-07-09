from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    AttendanceSessionViewSet,
    AttendanceViewSet,
    MarkAttendanceAPIView,
    StudentsByScheduleAPIView,
    AttendanceHistoryAPIView,
)

router = DefaultRouter()

router.register(
    r"sessions",
    AttendanceSessionViewSet,
    basename="attendance-session",
)

router.register(
    r"records",
    AttendanceViewSet,
    basename="attendance",
)

urlpatterns = [
    path("", include(router.urls)),

    path(
        "mark/",
        MarkAttendanceAPIView.as_view(),
        name="mark-attendance",
    ),

    path(
        "schedule/<int:schedule_id>/students/",
        StudentsByScheduleAPIView.as_view(),
        name="students-by-schedule",
    ),

    path(
        "session/<int:session_id>/",
        AttendanceHistoryAPIView.as_view(),
        name="attendance-history",
    ),
]
