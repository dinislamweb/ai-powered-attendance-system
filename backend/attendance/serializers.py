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