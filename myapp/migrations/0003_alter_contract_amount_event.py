# Generated by Django 4.1.3 on 2022-12-05 09:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("myapp", "0002_contract"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contract",
            name="amount",
            field=models.FloatField(verbose_name="Montant en euros"),
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date_created",
                    models.DateField(
                        auto_now_add=True, verbose_name="Date de création"
                    ),
                ),
                (
                    "date_updated",
                    models.DateField(
                        auto_now_add=True, verbose_name="Date de modification"
                    ),
                ),
                (
                    "event_status",
                    models.CharField(
                        choices=[("CREATED", "Créé"), ("FINISHED", "Terminé")],
                        max_length=20,
                        verbose_name="Statut de l'évènement",
                    ),
                ),
                (
                    "attendees",
                    models.IntegerField(verbose_name="Nombre de participants"),
                ),
                ("event_date", models.DateField(verbose_name="Date de l'évènement")),
                (
                    "notes",
                    models.TextField(blank=True, null=True, verbose_name="Notes"),
                ),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.client",
                        verbose_name="Client",
                    ),
                ),
                (
                    "support_contact",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Responsable",
                    ),
                ),
            ],
        ),
    ]
