# Generated by Django 4.1.1 on 2022-10-09 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("carrier", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Cargo",
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
                    "cargo_type",
                    models.CharField(
                        choices=[
                            ("Automobile Goods", "Automobile Goods"),
                            ("Industry", "Industry"),
                            ("Industry ADR", "Industry ADR"),
                            ("Industry Temp", "Industry Temp"),
                            ("Industry Temp ADR", "Industry Temp ADR"),
                            ("Consumer Goods", "Consumer Goods"),
                            ("Frozen Goods", "Frozen Goods"),
                            ("Frozen Food", "Frozen Food"),
                            ("Dry Food", "Dry Food"),
                            ("Fruits & Vegetables", "Fruits & Vegetables"),
                            ("Pet Food", "Pet Food"),
                            ("Waste", "Waste"),
                            ("Pharmacy", "Pharmacy"),
                            ("Empties", "Empties"),
                            ("Furniture", "Furniture"),
                        ],
                        default="Industry",
                        max_length=50,
                        null=True,
                    ),
                ),
                ("length", models.FloatField(null=True)),
                ("weight", models.FloatField(null=True)),
                ("adr", models.BooleanField(default=False, null=True)),
                ("waste", models.BooleanField(default=False, null=True)),
            ],
            options={
                "verbose_name": "Cargo",
                "verbose_name_plural": "Cargo",
            },
        ),
        migrations.CreateModel(
            name="Order",
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
                    "order_id",
                    models.UUIDField(
                        db_index=True, default=uuid.uuid4, editable=False, unique=True
                    ),
                ),
                (
                    "loading_place",
                    django_countries.fields.CountryField(max_length=746, multiple=True),
                ),
                ("loading_date", models.DateTimeField(null=True)),
                (
                    "delivery_place",
                    django_countries.fields.CountryField(max_length=746, multiple=True),
                ),
                ("delivery_date", models.DateTimeField(null=True)),
                ("distance", models.FloatField(blank=True)),
                (
                    "currency",
                    models.CharField(
                        choices=[("EUR", "EUR"), ("USD", "USD")],
                        default="EUR",
                        max_length=5,
                        null=True,
                    ),
                ),
                (
                    "proposed_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=12, null=True
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Actual", "Actual"),
                            ("Confirmed", "Confirmed"),
                            ("Delivery", "Delivery"),
                            ("Closed", "Closed"),
                        ],
                        default="Actual",
                        max_length=10,
                    ),
                ),
                ("remarks", models.TextField(blank=True)),
                (
                    "cargo_details",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cargo_details",
                        to="shipper.cargo",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "vehicle_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vehicle_type",
                        to="carrier.vehicle",
                    ),
                ),
            ],
            options={
                "verbose_name": "Order",
                "verbose_name_plural": "Orders",
            },
        ),
    ]
