from django.db import models


class Course(models.Model):
    STATUS_CHOICES = (
        ("active", "Active"),
        ("inactive", "Inactive"),
    )

    course_name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    duration = models.CharField(max_length=100)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="active",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["course_name"]
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.course_name