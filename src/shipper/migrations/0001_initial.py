# Generated by Django 4.1.1 on 2022-11-20 13:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("carrier", "0001_initial"),
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
                    "order_id",
                    models.UUIDField(
                        db_index=True,
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("company_name", models.CharField(max_length=100, null=True)),
                ("contact_person", models.CharField(max_length=100, null=True)),
                ("email", models.EmailField(max_length=255, null=True)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, null=True, region=None
                    ),
                ),
                ("loading_country", django_countries.fields.CountryField(max_length=2)),
                ("loading_postcode", models.CharField(max_length=25, null=True)),
                ("loading_city", models.CharField(max_length=100, null=True)),
                (
                    "loading_address",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "loading_coordinates",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("loading_date", models.DateTimeField(null=True)),
                (
                    "delivery_country",
                    django_countries.fields.CountryField(max_length=2),
                ),
                ("delivery_postcode", models.CharField(max_length=25, null=True)),
                ("delivery_city", models.CharField(max_length=100, null=True)),
                (
                    "delivery_address",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "delivery_coordinates",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("delivery_date", models.DateTimeField(null=True)),
                ("distance", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "length",
                    models.FloatField(
                        null=True,
                        validators=[django.core.validators.MaxValueValidator(13.6)],
                    ),
                ),
                (
                    "weight",
                    models.FloatField(
                        null=True,
                        validators=[django.core.validators.MaxValueValidator(24.0)],
                    ),
                ),
                ("adr", models.BooleanField(default=False, null=True)),
                ("waste", models.BooleanField(default=False, null=True)),
                (
                    "currency",
                    models.CharField(
                        choices=[("EUR", "EUR"), ("USD", "USD")],
                        default="EUR",
                        max_length=5,
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
                ("remarks", models.TextField(blank=True, null=True)),
                (
                    "cargo_details",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cargo_details",
                        to="shipper.cargo",
                    ),
                ),
                (
                    "trailer_type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trailer_type",
                        to="carrier.trailer",
                    ),
                ),
            ],
            options={
                "verbose_name": "Order",
                "verbose_name_plural": "Orders",
            },
        ),
    ]
