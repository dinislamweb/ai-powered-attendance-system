from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    AttendanceSessionViewSet,
    AttendanceViewSet,
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
]