from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import permissions


class IsReadOnlyUser(BasePermission):
    def has_permission(self, request, view):
        # Allow access if the request method is in SAFE_METHODS (GET, HEAD, OPTIONS)
        return request.method in SAFE_METHODS


class IsWorkoutPlanOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
