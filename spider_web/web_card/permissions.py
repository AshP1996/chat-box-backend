# permissions.py
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            custom_user_id = request.user.id
            return custom_user_id == obj.user_id_id
        except AttributeError:
            return False