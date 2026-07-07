from django.contrib import admin
from .models import Batch


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = (
        "batch_code",
        "batch_name",
        "course",
        "start_date",
        "end_date",
        "status",
    )

    list_filter = (
        "status",
        "course",
    )

    search_fields = (
        "batch_code",
        "batch_name",
    )

    ordering = (
        "batch_name",
    )