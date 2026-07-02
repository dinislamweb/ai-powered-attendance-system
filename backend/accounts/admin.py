from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Teacher, Student


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "role",
        "is_staff",
        "is_active",
    )

    list_filter = (
        "role",
        "is_staff",
        "is_active",
    )

    search_fields = (
        "username",
        "email",
    )

    ordering = ("id",)

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Information",
            {
                "fields": (
                    "role",
                )
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Custom Information",
            {
                "fields": (
                    "email",
                    "role",
                )
            },
        ),
    )


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        "employee_id",
        "user",
        "phone",
    )

    search_fields = (
        "employee_id",
        "user__username",
        "user__email",
    )


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "student_id",
        "user",
        "batch",
    )

    search_fields = (
        "student_id",
        "user__username",
        "user__email",
        "batch",
    )