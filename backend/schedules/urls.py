from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ScheduleViewSet,
    MyScheduleAPIView,
)

router = DefaultRouter()
router.register(r"", ScheduleViewSet)

urlpatterns = [
    path("my-schedules/", MyScheduleAPIView.as_view()),
    path("", include(router.urls)),
]