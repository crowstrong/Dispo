import uuid

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField


class Order(models.Model):
    class STATUS_CHOICE(models.TextChoices):
        ACTUAL = "Actual", "Actual"
        CONFIRMED = "Confirmed", "Confirmed"
        Delivery = "Delivery", "Delivery"
        CLOSE = "Closed", "Closed"

    class CURRENCY_CHOICE(models.TextChoices):
        EU = "EUR", "EUR"
        USD = "USD", "USD"

    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    order_id = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
    loading_place = CountryField(multiple=True, blank=False)
    loading_date = models.DateTimeField(blank=False, null=True)
    delivery_place = CountryField(multiple=True, blank=False)
    delivery_date = models.DateTimeField(blank=False, null=True)
    distance = models.FloatField(blank=True)
    vehicle_type = models.ForeignKey(
        to="carrier.Vehicle", related_name="vehicle_type", on_delete=models.CASCADE, blank=False
    )
    cargo_details = models.ForeignKey(
        to="shipper.Cargo", related_name="cargo_details", on_delete=models.CASCADE, blank=False
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICE.choices, default=CURRENCY_CHOICE.EU, max_length=5, blank=False, null=True
    )
    proposed_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICE.choices, default=STATUS_CHOICE.ACTUAL, max_length=10)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")


class Cargo(models.Model):
    class CARGO_TYPES(models.TextChoices):
        AUTOMOBILE = "Automobile Goods", "Automobile Goods"
        INDUSTRY = "Industry", "Industry"
        INDUSTRY_ADR = "Industry ADR", "Industry ADR"
        INDUSTRY_TEMP = "Industry Temp", "Industry Temp"
        INDUSTRY_TEMP_ADR = "Industry Temp ADR", "Industry Temp ADR"
        CONSUMER_GOODS = "Consumer Goods", "Consumer Goods"
        FROZEN_GOODS = "Frozen Goods", "Frozen Goods"
        FROZEN_FOOD = "Frozen Food", "Frozen Food"
        DRY_FOOD = "Dry Food", "Dry Food"
        FRUITS_VEGETABLES = "Fruits & Vegetables", "Fruits & Vegetables"
        PET_FOOD = "Pet Food", "Pet Food"
        WASTE = "Waste", "Waste"
        PHARMACY = "Pharmacy", "Pharmacy"
        EMPTIES = "Empties", "Empties"
        FURNITURE = "Furniture", "Furniture"

    cargo_type = models.CharField(
        choices=CARGO_TYPES.choices, default=CARGO_TYPES.INDUSTRY, max_length=50, blank=False, null=True
    )
    length = models.FloatField(blank=False, null=True, validators=[MaxValueValidator(13.6)])
    weight = models.FloatField(blank=False, null=True, validators=[MaxValueValidator(24.0)])
    adr = models.BooleanField(default=False, null=True)
    waste = models.BooleanField(default=False, null=True)

    def __str__(self):
        return f"{self.cargo_type} {self.length} {self.weight}"

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Cargo")
        verbose_name_plural = _("Cargo")
