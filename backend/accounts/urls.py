from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    LoginAPIView,
    CurrentUserAPIView,
    UserViewSet,
    TeacherViewSet,
    StudentViewSet,
)
router = DefaultRouter()

router.register(r"users", UserViewSet, basename="user")
router.register(r"teachers", TeacherViewSet, basename="teacher")
router.register(r"students", StudentViewSet, basename="student")

urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),
    path("me/", CurrentUserAPIView.as_view(), name="current-user"),
    path("", include(router.urls)),
]