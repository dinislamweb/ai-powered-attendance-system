from django.db import models

from schedules.models import Schedule
from accounts.models import Teacher, Student


class AttendanceSession(models.Model):
    schedule = models.ForeignKey(
        Schedule,
        on_delete=models.CASCADE,
        related_name="attendance_sessions",
    )

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name="attendance_sessions",
    )

    date = models.DateField()

    remarks = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-date"]
        verbose_name = "Attendance Session"
        verbose_name_plural = "Attendance Sessions"

    def __str__(self):
        return f"{self.schedule} ({self.date})"


class Attendance(models.Model):

    STATUS_CHOICES = (
        ("present", "Present"),
        ("absent", "Absent"),
    )

    session = models.ForeignKey(
        AttendanceSession,
        on_delete=models.CASCADE,
        related_name="attendance_records",
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="attendance_records",
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="present",
    )

    marked_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ("session", "student")
        ordering = ["student__student_id"]
        verbose_name = "Attendance"
        verbose_name_plural = "Attendance"

    def __str__(self):
        return f"{self.student.student_id} - {self.status}"