from rest_framework.viewsets import ModelViewSet

from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeViewset(ModelViewSet):

    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.all()


class SignupViewset(ModelViewSet):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return []
