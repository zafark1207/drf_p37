from rest_framework.permissions import BasePermission, SAFE_METHODS

from apps.models import Post


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user




class CustomPostPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if request.method == 'POST':
            return request.user and request.user.is_authenticated

        return True

    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            return request.user and request.user.is_staff

        if request.method in ['PUT', 'PATCH']:
            return obj.author == request.user or request.user.is_staff

        return True
