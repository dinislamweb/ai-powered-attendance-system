from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from batches.models import Batch


class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("teacher", "Teacher"),
        ("student", "Student"),
    )

    email = models.EmailField(unique=True)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="student"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email} ({self.role})"


class Teacher(models.Model):
    STATUS_CHOICES = (
        ("active", "Active"),
        ("inactive", "Inactive"),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="teacher_profile"
    )

    employee_id = models.CharField(max_length=30, unique=True)
    phone = models.CharField(max_length=20, blank=True)
    designation = models.CharField(max_length=100, blank=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="active"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee_id} - {self.user.get_full_name() or self.user.username}"
    
class Student(models.Model):
    STATUS_CHOICES = (
        ("active", "Active"),
        ("inactive", "Inactive"),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )

    student_id = models.CharField(max_length=30, unique=True)

    batch = models.ForeignKey(
        Batch,
        on_delete=models.CASCADE,
        related_name="students"
    )

    phone = models.CharField(max_length=20, blank=True)

    admission_date = models.DateField(
    null=True,
    blank=True,
)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="active"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student_id} - {self.user.get_full_name() or self.user.username}"