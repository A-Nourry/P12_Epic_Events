from rest_framework.serializers import ModelSerializer
from .models import Client, Contract, Event


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "mobile",
            "company_name",
            "date_created",
            "date_updated",
            "sales_contact",
        ]


class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = [
            "id",
            "sales_contact",
            "client",
            "date_created",
            "date_updated",
            "status",
            "amount",
            "payement_due",
        ]


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "client",
            "date_created",
            "date_updated",
            "support_contact",
            "event_status",
            "attendees",
            "event_date",
            "notes",
        ]
