from rest_framework import permissions

class IsAuthenticatedOwnerorUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if request.user == obj.user:
            return True
        return False