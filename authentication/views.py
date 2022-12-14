from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Employee
from .serializers import EmployeeSerializer
from .permissions import IsManager


class EmployeeViewset(ModelViewSet):

    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated & IsManager]
    filterset_fields = ["last_name", "user_team"]
    search_fields = ["last_name", "user_team"]

    def get_queryset(self):
        return Employee.objects.all()
