from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include


def home(request):
    return JsonResponse({"message": "Student Attendance Management System API is running."})


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/accounts/", include("accounts.urls")),
    path("api/courses/", include("courses.urls")),
    path("api/batches/", include("batches.urls")),
    path("api/schedules/", include("schedules.urls")),
    path("api/attendance/", include("attendance.urls")),
    path("api/dashboard/", include("dashboard.urls")),
]


