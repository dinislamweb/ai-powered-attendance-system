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

    def validate(self, attrs):
        start = attrs["start_time"]
        end = attrs["end_time"]

        # End time must be greater than start time
        if start >= end:
            raise serializers.ValidationError(
                {
                    "end_time": "End time must be after start time."
                }
            )

        teacher = attrs["teacher"]
        day = attrs["day"]

        queryset = Schedule.objects.filter(
            teacher=teacher,
            day=day,
            start_time=start,
        )

        # Exclude current object while updating
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError(
                {
                    "schedule": "This schedule already exists."
                }
            )

        return attrs