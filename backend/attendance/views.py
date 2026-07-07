from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import AttendanceSession, Attendance
from .serializers import (
    AttendanceSessionSerializer,
    AttendanceSerializer,
)


class AttendanceSessionViewSet(viewsets.ModelViewSet):
    queryset = AttendanceSession.objects.all()
    serializer_class = AttendanceSessionSerializer
    permission_classes = [IsAuthenticated]


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]