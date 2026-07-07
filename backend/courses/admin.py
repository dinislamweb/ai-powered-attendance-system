from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "course_name",
        "duration",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
    )

    search_fields = (
        "course_name",
    )

    ordering = (
        "course_name",
    )