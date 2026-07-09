from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Schedule
from .serializers import ScheduleSerializer

from accounts.models import Teacher

from permissions.permissions import (
    IsAdmin,
    IsTeacher,
)


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [
        IsAuthenticated,
        IsAdmin,
    ]


class MyScheduleAPIView(APIView):
    permission_classes = [
        IsAuthenticated,
        IsTeacher,
    ]

    def get(self, request):
        try:
            teacher = Teacher.objects.get(user=request.user)
        except Teacher.DoesNotExist:
            return Response(
                {"message": "Teacher profile not found."},
                status=404,
            )

        schedules = Schedule.objects.filter(
            teacher=teacher,
            status="active",
        )

        serializer = ScheduleSerializer(
            schedules,
            many=True,
        )

        return Response(serializer.data)