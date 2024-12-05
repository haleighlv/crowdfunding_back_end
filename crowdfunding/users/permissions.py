from rest_framework import permissions

class IsAuthenticatedOwnerorUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if request.user == obj.user:
            return True
        return False

class IsUserOrAdminOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow admin users
        if request.user.is_staff:
            return True
            
        # Allow the user themselves
        return obj == request.user