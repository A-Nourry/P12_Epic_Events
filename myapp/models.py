from django.db import models
from django.conf import settings


class Client(models.Model):
    first_name = models.CharField(max_length=25, verbose_name="Prénom")
    last_name = models.CharField(max_length=25, verbose_name="Nom")
    email = models.EmailField(
        max_length=100, blank=True, null=True, unique=True, verbose_name="Email"
    )
    phone = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Téléphone"
    )
    mobile = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Mobile"
    )
    company_name = models.CharField(max_length=250, verbose_name="Entreprise")
    date_created = models.DateField(
        auto_now_add=True, verbose_name="Date d'inscription"
    )
    date_updated = models.DateField(auto_now=True, verbose_name="Date de modification")
    sales_contact = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Vendeur(se)",
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
