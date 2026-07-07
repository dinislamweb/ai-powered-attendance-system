from django.db import models
from courses.models import Course


class Batch(models.Model):
    STATUS_CHOICES = (
        ("active", "Active"),
        ("inactive", "Inactive"),
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="batches",
    )

    batch_code = models.CharField(max_length=20, unique=True)
    batch_name = models.CharField(max_length=150)

    description = models.TextField(blank=True)

    start_date = models.DateField()
    end_date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="active",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["batch_name"]
        verbose_name = "Batch"
        verbose_name_plural = "Batches"

    def __str__(self):
        return f"{self.batch_code} - {self.batch_name}"