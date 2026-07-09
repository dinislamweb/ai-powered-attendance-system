from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Attendance, AttendanceSession
from schedules.models import Schedule
from accounts.models import Student
from accounts.serializers import StudentSerializer

from .serializers import (
    AttendanceSessionSerializer,
    AttendanceSerializer,
    MarkAttendanceSerializer,
    AttendanceHistorySerializer,
)

from permissions.permissions import (
    IsAdmin,
    IsTeacher,
)


class AttendanceSessionViewSet(viewsets.ModelViewSet):
    queryset = AttendanceSession.objects.all()
    serializer_class = AttendanceSessionSerializer
    permission_classes = [
        IsAuthenticated,
        IsAdmin,
    ]


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [
        IsAuthenticated,
        IsAdmin,
    ]


class MarkAttendanceAPIView(APIView):
    permission_classes = [
        IsAuthenticated,
        IsTeacher,
    ]

    def post(self, request):

        serializer = MarkAttendanceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        schedule = Schedule.objects.get(
            id=serializer.validated_data["schedule"]
        )

        attendance_date = serializer.validated_data["date"]

        teacher = schedule.teacher

        session, created = AttendanceSession.objects.get_or_create(
            schedule=schedule,
            teacher=teacher,
            date=attendance_date,
        )

        students = serializer.validated_data["students"]

        for item in students:

            student = Student.objects.get(
                id=item["student"]
            )

            Attendance.objects.update_or_create(
                session=session,
                student=student,
                defaults={
                    "status": item["status"]
                }
            )

        return Response(
            {
                "message": "Attendance submitted successfully."
            }
        )


class StudentsByScheduleAPIView(APIView):
    permission_classes = [
        IsAuthenticated,
        IsTeacher,
    ]

    def get(self, request, schedule_id):

        try:
            schedule = Schedule.objects.get(id=schedule_id)
        except Schedule.DoesNotExist:
            return Response(
                {"message": "Schedule not found."},
                status=404,
            )

        students = Student.objects.filter(
            batch=schedule.batch,
            status="active",
        )

        serializer = StudentSerializer(
            students,
            many=True,
        )

        return Response(serializer.data)


class AttendanceHistoryAPIView(APIView):
    permission_classes = [
        IsAuthenticated,
        IsTeacher,
    ]

    def get(self, request, session_id):

        try:
            session = AttendanceSession.objects.get(id=session_id)
        except AttendanceSession.DoesNotExist:
            return Response(
                {"message": "Attendance session not found."},
                status=404,
            )

        records = Attendance.objects.filter(
            session=session
        )

        serializer = AttendanceHistorySerializer(
            records,
            many=True,
        )

        return Response(
            {
                "session_id": session.id,
                "date": session.date,
                "schedule": session.schedule.id,
                "teacher": session.teacher.user.get_full_name(),
                "records": serializer.data,
            }
        )