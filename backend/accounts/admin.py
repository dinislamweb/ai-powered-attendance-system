from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Teacher, Student


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    list_display = (
        "email",
        "username",
        "first_name",
        "last_name",
        "role",
        "is_active",
        "is_staff",
        "created_at",
    )

    list_filter = (
        "role",
        "is_active",
        "is_staff",
    )

    search_fields = (
        "email",
        "username",
        "first_name",
        "last_name",
    )

    ordering = ("email",)

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "username",
                    "password",
                )
            },
        ),
        (
            "Personal Information",
            {
                "fields": (
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            "Role",
            {
                "fields": (
                    "role",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "Important Dates",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "first_name",
                    "last_name",
                    "role",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        "employee_id",
        "get_name",
        "get_email",
        "designation",
        "phone",
        "status",
    )

    search_fields = (
        "employee_id",
        "user__first_name",
        "user__last_name",
        "user__email",
    )

    list_filter = (
        "status",
        "designation",
    )

    ordering = (
        "employee_id",
    )

    def get_name(self, obj):
        return obj.user.get_full_name() or obj.user.username

    get_name.short_description = "Name"

    def get_email(self, obj):
        return obj.user.email

    get_email.short_description = "Email"


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "student_id",
        "get_name",
        "batch",
        "phone",
        "status",
    )

    search_fields = (
        "student_id",
        "user__first_name",
        "user__last_name",
        "user__email",
    )

    list_filter = (
        "batch",
        "status",
    )

    ordering = (
        "student_id",
    )

    def get_name(self, obj):
        return obj.user.get_full_name() or obj.user.username

    get_name.short_description = "Name"