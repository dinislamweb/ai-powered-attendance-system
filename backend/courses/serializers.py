
from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"

    def validate_course_code(self, value):
        value = value.strip().upper()

        queryset = Course.objects.filter(course_code=value)

        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError(
                "Course code already exists."
            )

        return value

    def validate_course_name(self, value):
        return value.strip()