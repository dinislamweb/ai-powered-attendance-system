from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    Allows access only to admin users.
    """
    message = "Only admin users can access this resource."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "admin"
        )


class IsTeacher(BasePermission):
    """
    Allows access only to teacher users.
    """
    message = "Only teacher users can access this resource."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "teacher"
        )


class IsStudent(BasePermission):
    """
    Allows access only to student users.
    """
    message = "Only student users can access this resource."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "student"
        )