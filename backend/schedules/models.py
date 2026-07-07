from django.db import models
from accounts.models import Teacher
from courses.models import Course
from batches.models import Batch


class Schedule(models.Model):
    DAY_CHOICES = (
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday"),
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
    )

    STATUS_CHOICES = (
        ("active", "Active"),
        ("inactive", "Inactive"),
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="schedules",
    )

    batch = models.ForeignKey(
        Batch,
        on_delete=models.CASCADE,
        related_name="schedules",
    )

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name="schedules",
    )

    day = models.CharField(
        max_length=20,
        choices=DAY_CHOICES,
    )

    start_time = models.TimeField()

    end_time = models.TimeField()

    room = models.CharField(
        max_length=100,
        blank=True,
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="active",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["day", "start_time"]
        verbose_name = "Schedule"
        verbose_name_plural = "Schedules"

    def __str__(self):
        return f"{self.course} | {self.batch} | {self.teacher}"