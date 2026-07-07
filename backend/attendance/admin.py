from django.contrib import admin
from .models import AttendanceSession, Attendance


@admin.register(AttendanceSession)
class AttendanceSessionAdmin(admin.ModelAdmin):
    list_display = (
        "schedule",
        "teacher",
        "date",
        "created_at",
    )

    list_filter = (
        "date",
        "teacher",
    )

    search_fields = (
        "teacher__user__first_name",
        "teacher__user__last_name",
        "schedule__batch__batch_name",
    )

    ordering = ("-date",)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "session",
        "status",
        "marked_at",
    )

    list_filter = (
        "status",
        "session",
    )

    search_fields = (
        "student__student_id",
        "student__user__first_name",
        "student__user__last_name",
    )

    ordering = ("-marked_at",)