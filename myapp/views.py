from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import PermissionDenied

from .models import Client, Contract, Event
from authentication.permissions import IsManager, IsSupport, IsSeller
from .serializers import ClientSerializer, ContractSerializer, EventSerializer


class ClientViewset(ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated & IsManager | IsSeller | IsSupport]
    filterset_fields = ["last_name", "email"]
    search_fields = ["last_name", "email"]

    def get_queryset(self):
        user = self.request.user

        if user.user_team == "MANAGEMENT":
            return Client.objects.all()

        if user.user_team == "SALES":
            return Client.objects.filter(sales_contact=user)

        if user.user_team == "SUPPORT":
            event = Event.objects.get(support_contact=user)
            return Client.objects.filter(id=event.client.id)

        raise PermissionDenied


class ContractViewset(ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated & IsManager | IsSeller]
    filterset_fields = ["date_created", "date_updated", "amount"]
    search_fields = ["date_created", "date_updated", "amount"]

    def get_queryset(self):
        user = self.request.user

        if user.user_team == 'MANAGEMENT':
            return Contract.objects.all()

        if user.user_team == 'SALES':
            return Contract.objects.filter(sales_contact=user)

        raise PermissionDenied


class EventViewset(ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated & IsManager | IsSeller | IsSupport]
    filterset_fields = ["client_id__last_name", "client_id__email", "date_created"]
    search_fields = ["client_id__last_name", "client_id__email", "date_created"]

    def get_queryset(self):
        user = self.request.user
        client = Client.objects.filter(sales_contact=user)

        if user.user_team == 'MANAGEMENT':
            return Event.objects.all()

        if user.user_team == "SALES":
            return Event.objects.filter(client__in=client)

        if user.user_team == 'SUPPORT':
            return Event.objects.filter(support_contact=user)

        raise PermissionDenied
