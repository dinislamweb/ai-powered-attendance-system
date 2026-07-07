from rest_framework import serializers
from .models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(
        source="teacher.user.get_full_name",
        read_only=True,
    )

    batch_name = serializers.CharField(
        source="batch.batch_name",
        read_only=True,
    )

    course_name = serializers.CharField(
        source="course.course_name",
        read_only=True,
    )

    class Meta:
        model = Schedule
        fields = [
            "id",
            "course",
            "course_name",
            "batch",
            "batch_name",
            "teacher",
            "teacher_name",
            "day",
            "start_time",
            "end_time",
            "room",
            "status",
        ]