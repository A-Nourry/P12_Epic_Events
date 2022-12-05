from rest_framework.viewsets import ModelViewSet


from .models import Client, Contract, Event
from .serializers import ClientSerializer, ContractSerializer, EventSerializer


class ClientViewset(ModelViewSet):
    serializer_class = ClientSerializer

    def get_queryset(self):
        return Client.objects.all()


class ContractViewset(ModelViewSet):
    serializer_class = ContractSerializer

    def get_queryset(self):
        return Contract.objects.all()


class EventViewset(ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()
