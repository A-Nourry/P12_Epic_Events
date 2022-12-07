from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Employee
from .serializers import EmployeeSerializer
from .permissions import IsManager


class EmployeeViewset(ModelViewSet):

    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated & IsManager]

    def get_queryset(self):
        return Employee.objects.all()
