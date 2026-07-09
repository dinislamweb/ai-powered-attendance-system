from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from accounts.models import Teacher, Student
from courses.models import Course
from batches.models import Batch
from schedules.models import Schedule
from attendance.models import Attendance, AttendanceSession

from permissions.permissions import (
    IsAdmin,
    IsTeacher,
    IsStudent,
)


class AdminDashboardAPIView(APIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin,
    ]

    def get(self, request):
        data = {
            "total_students": Student.objects.count(),
            "total_teachers": Teacher.objects.count(),
            "total_courses": Course.objects.count(),
            "total_batches": Batch.objects.count(),
            "total_schedules": Schedule.objects.count(),
            "attendance_sessions": AttendanceSession.objects.count(),
        }

        return Response(data)


class TeacherDashboardAPIView(APIView):
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
            teacher=teacher
        )

        total_students = Student.objects.filter(
            batch__in=schedules.values_list(
                "batch",
                flat=True,
            )
        ).distinct().count()

        attendance_sessions = AttendanceSession.objects.filter(
            teacher=teacher
        ).count()

        data = {
            "teacher_name": teacher.user.get_full_name(),
            "employee_id": teacher.employee_id,
            "assigned_schedules": schedules.count(),
            "total_students": total_students,
            "attendance_sessions": attendance_sessions,
        }

        return Response(data)


class StudentDashboardAPIView(APIView):
    permission_classes = [
        IsAuthenticated,
        IsStudent,
    ]

    def get(self, request):
        try:
            student = Student.objects.get(user=request.user)
        except Student.DoesNotExist:
            return Response(
                {"message": "Student profile not found."},
                status=404,
            )

        total_classes = Attendance.objects.filter(
            student=student
        ).count()

        present = Attendance.objects.filter(
            student=student,
            status="present",
        ).count()

        absent = Attendance.objects.filter(
            student=student,
            status="absent",
        ).count()

        attendance_percentage = (
            round((present / total_classes) * 100, 2)
            if total_classes > 0
            else 0
        )

        data = {
            "student_name": student.user.get_full_name(),
            "student_id": student.student_id,
            "batch": student.batch.batch_name,
            "present": present,
            "absent": absent,
            "total_classes": total_classes,
            "attendance_percentage": attendance_percentage,
        }

        return Response(data)