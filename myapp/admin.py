from django.contrib import admin
from .models import Client


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


admin.site.register(Client, ClientAdmin)
