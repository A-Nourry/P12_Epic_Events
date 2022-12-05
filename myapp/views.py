from rest_framework.viewsets import ModelViewSet


from .models import Client, Contract
from .serializers import ClientSerializer, ContractSerializer


class ClientViewset(ModelViewSet):
    serializer_class = ClientSerializer

    def get_queryset(self):
        return Client.objects.all()


class ContractViewset(ModelViewSet):
    serializer_class = ContractSerializer

    def get_queryset(self):
        return Contract.objects.all()
