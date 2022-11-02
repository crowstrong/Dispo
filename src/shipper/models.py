import random
import uuid

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from faker import Faker

from carrier.models import Trailer


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

    def __str__(self):
        return f"{self.cargo_type}"

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Cargo")
        verbose_name_plural = _("Cargo")


class Order(models.Model):
    class STATUS_CHOICE(models.TextChoices):
        ACTUAL = "Actual", "Actual"
        CONFIRMED = "Confirmed", "Confirmed"
        Delivery = "Delivery", "Delivery"
        CLOSE = "Closed", "Closed"

    class CURRENCY_CHOICE(models.TextChoices):
        EU = "EUR", "EUR"
        USD = "USD", "USD"

    order_id = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
    company_name = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    contact_person = models.CharField(max_length=100, blank=False, null=True)
    contact_email = models.EmailField(max_length=255, blank=False, null=True)
    loading_country = CountryField(blank_label="(select country)", blank=False)
    loading_postcode = models.CharField(validators=[MinValueValidator(5)], max_length=25, blank=False, null=True)
    loading_city = models.CharField(max_length=100, blank=False, null=True)
    loading_address = models.CharField(max_length=255, blank=True, null=True)
    loading_coordinates = models.CharField(max_length=255, blank=True, null=True)
    loading_date = models.DateTimeField(blank=False, null=True)
    delivery_country = CountryField(blank_label="(select country)", blank=False)
    delivery_postcode = models.CharField(validators=[MinValueValidator(5)], max_length=25, blank=False, null=True)
    delivery_city = models.CharField(max_length=100, blank=False, null=True)
    delivery_address = models.CharField(max_length=255, blank=True, null=True)
    delivery_coordinates = models.CharField(max_length=255, blank=True, null=True)
    delivery_date = models.DateTimeField(blank=False, null=True)
    distance = models.CharField(max_length=255, blank=True, null=True)
    trailer_details = models.ForeignKey(
        to="carrier.Trailer", related_name="trailer_type", on_delete=models.CASCADE, blank=False, null=True)
    cargo_details = models.ForeignKey(
        to="shipper.Cargo", related_name="cargo_details", on_delete=models.CASCADE, blank=False
    )
    length = models.FloatField(blank=False, null=True, validators=[MaxValueValidator(13.6)])
    weight = models.FloatField(blank=False, null=True, validators=[MaxValueValidator(24.0)])
    adr = models.BooleanField(default=False, null=True)
    waste = models.BooleanField(default=False, null=True)
    currency = models.CharField(choices=CURRENCY_CHOICE.choices, default=CURRENCY_CHOICE.EU, max_length=5, blank=False)
    proposed_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICE.choices, default=STATUS_CHOICE.ACTUAL, max_length=10)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.company_name} {self.loading_date} {self.loading_country} {self.loading_postcode} " \
               f"{self.loading_city} {self.delivery_date} {self.delivery_country} {self.delivery_postcode} " \
               f"{self.delivery_city} "

    # @classmethod
    # def generate_instances(cls, count: int) -> None:
    #     fake = Faker()
    #     for _ in range(count):
    #         cls.objects.create(
    #             order_id=fake.uuid4(),
    #             company_name=fake.company(),
    #             contact_person=fake.name(),
    #             contact_email=fake.company_email(),
    #             loading_country=fake.country(),
    #             loading_postcode=fake.postcode(),
    #             loading_city=fake.city(),
    #             loading_address=fake.street_address(),
    #             loading_coordinates=fake.latlng(),
    #             loading_date=fake.iso8601(),
    #             delivery_country=fake.country(),
    #             delivery_postcode=fake.postcode(),
    #             delivery_city=fake.city(),
    #             delivery_address=fake.street_address(),
    #             delivery_coordinates=fake.latlng(),
    #             delivery_date=fake.iso8601(),
    #             distance=round(random.uniform(500.0, 1500.0), 1),
    #             trailer_details=random.choice(Trailer.trailer),
    #             cargo_details=random.choice(Cargo.cargo_type),
    #             length=random.uniform(8.0, 13.6),
    #             weight=random.uniform(10.0, 24.0),
    #             adr=fake.pybool(),
    #             waste=fake.pybool(),
    #             currency=random.choice(Order.currency),
    #             proposed_price=round(random.uniform(500.00, 5000.00), 2),
    #             status=random.choice(Order.status),
    #             remarks=fake.word(),
    #         )

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
