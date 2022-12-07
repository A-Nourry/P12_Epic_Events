from rest_framework.permissions import BasePermission

from myapp.models import Event, Client, Contract
from .models import Employee

MANAGER_AUTHORIZED_METHOD = ("GET", "PUT")
SELLER_AUTHORIZED_METHOD = ("GET", "POST", "PUT")
SUPPORT_AUTHORIZED_METHOD = ("GET", "PUT")


class IsSupport(BasePermission):
    def has_permission(self, request, view):
        if request.method in SUPPORT_AUTHORIZED_METHOD:
            if request.user.user_team == "SUPPORT":
                return True

    def has_object_permission(self, request, view, obj):
        if type(obj) is Client:
            if request.method == "GET":
                return True

        if type(obj) is Event:
            if request.method == "POST":
                return False

            elif request.method == "GET":
                if request.user.id == obj.support_contact.id:
                    return True

            elif request.method == "PUT":
                if (
                    request.user.id == obj.support_contact.id
                    and obj.event_status == "CREATED"
                ):
                    return True


class IsSeller(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_team == "SALES":
            return True

    def has_object_permission(self, request, view, obj):
        if type(obj) is Client:
            if request.method in SELLER_AUTHORIZED_METHOD:
                return True

        elif type(obj) is Contract:
            if request.method in SELLER_AUTHORIZED_METHOD:
                return True

        if type(obj) is Event:
            if request.method == "GET" or request.method == "POST":
                return True


class IsManager(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_team == "MANAGEMENT":
            return True

    def has_object_permission(self, request, view, obj):
        if type(obj) is Employee:
            if request.user.user_team == "MANAGEMENT":
                return True
        else:
            if (
                request.user.user_team == "MANAGEMENT"
                and request.method in MANAGER_AUTHORIZED_METHOD
            ):
                return True
