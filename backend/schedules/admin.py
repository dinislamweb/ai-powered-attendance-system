from django.contrib import admin
from .models import Schedule


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):

    list_display = (
        "course",
        "batch",
        "teacher",
        "day",
        "start_time",
        "end_time",
        "room",
        "status",
    )

    search_fields = (
        "course__course_name",
        "batch__batch_name",
        "teacher__user__first_name",
        "teacher__user__last_name",
    )

    list_filter = (
        "day",
        "status",
        "course",
    )

    ordering = (
        "day",
        "start_time",
    )
