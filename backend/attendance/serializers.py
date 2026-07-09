from rest_framework import serializers

from .models import AttendanceSession, Attendance




class AttendanceSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceSession
        fields = "__all__"


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"
        

class AttendanceItemSerializer(serializers.Serializer):
    student = serializers.IntegerField()
    status = serializers.ChoiceField(
        choices=[
            ("present", "Present"),
            ("absent", "Absent"),
        ]
    )


class MarkAttendanceSerializer(serializers.Serializer):
    schedule = serializers.IntegerField()
    date = serializers.DateField()
    students = AttendanceItemSerializer(many=True)
    
from .models import Attendance


class AttendanceHistorySerializer(serializers.ModelSerializer):
    student_id = serializers.CharField(source="student.student_id", read_only=True)
    student_name = serializers.SerializerMethodField()

    class Meta:
        model = Attendance
        fields = [
            "id",
            "student_id",
            "student_name",
            "status",
            "marked_at",
        ]

    def get_student_name(self, obj):
        return obj.student.user.get_full_name()