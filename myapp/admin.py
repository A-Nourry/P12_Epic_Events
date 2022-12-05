from django.contrib import admin
from .models import Client, Contract, Event


class ClientAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "last_name",
        "first_name",
        "email",
        "company_name",
        "date_created",
        "date_updated",
        "sales_contact",
    )


class ContractAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "client",
        "sales_contact",
        "status",
        "date_created",
        "date_updated",
        "amount",
    )


class EventAdmin(admin.ModelAdmin):

    list_display = (
            "id",
            "client",
            "date_created",
            "date_updated",
            "support_contact",
            "event_status",
            "attendees",
            "event_date",
            "notes",
        )


admin.site.register(Client, ClientAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Event, EventAdmin)
