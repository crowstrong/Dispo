import random
import uuid

from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from faker import Faker

from accounts.models import Person
from carrier.models import Trailer


class Cargo(models.Model):
    CARGO_TYPES = (
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
        ("Furniture", "Furniture")
    )

    cargo_type = models.CharField(
        choices=CARGO_TYPES, default="INDUSTRY", max_length=50, blank=False, null=True
    )

    def __str__(self):
        return f"{self.cargo_type}"

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Cargo")
        verbose_name_plural = _("Cargo")


class Order(Person):
    STATUS_CHOICE = (
        ("Actual", "Actual"),
        ("Confirmed", "Confirmed"),
        ("Delivery", "Delivery"),
        ("Closed", "Closed"),
    )

    CURRENCY_CHOICE = (
        ("EUR", "EUR"),
        ("USD", "USD"),
    )

    order_id = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
    loading_country = CountryField(blank_label="(select country)", blank=False)
    loading_postcode = models.CharField(max_length=25, blank=False, null=True)
    loading_city = models.CharField(max_length=100, blank=False, null=True)
    loading_address = models.CharField(max_length=255, blank=True, null=True)
    loading_coordinates = models.CharField(max_length=255, blank=True, null=True)
    loading_date = models.DateTimeField(blank=False, null=True)
    delivery_country = CountryField(blank_label="(select country)", blank=False)
    delivery_postcode = models.CharField(max_length=25, blank=False, null=True)
    delivery_city = models.CharField(max_length=100, blank=False, null=True)
    delivery_address = models.CharField(max_length=255, blank=True, null=True)
    delivery_coordinates = models.CharField(max_length=255, blank=True, null=True)
    delivery_date = models.DateTimeField(blank=False, null=True)
    distance = models.CharField(max_length=255, blank=True, null=True)
    trailer_type = models.ForeignKey(
        to="carrier.Trailer", related_name="trailer_type", on_delete=models.CASCADE, blank=False, null=True
    )
    cargo_details = models.ForeignKey(
        to="shipper.Cargo", related_name="cargo_details", on_delete=models.CASCADE, blank=False
    )
    length = models.FloatField(blank=False, null=True, validators=[MaxValueValidator(13.6)])
    weight = models.FloatField(blank=False, null=True, validators=[MaxValueValidator(24.0)])
    adr = models.BooleanField(default=False, null=True)
    waste = models.BooleanField(default=False, null=True)
    currency = models.CharField(choices=CURRENCY_CHOICE, default="EU", max_length=5, blank=False)
    proposed_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICE, default="ACTUAL", max_length=10)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.company_name}"

    @classmethod
    def generate_instances(cls, count: int) -> None:
        fake = Faker()
        for _ in range(count):
            cls.objects.create(
                order_id=fake.uuid4(),
                company_name=fake.company(),
                contact_person=fake.name(),
                email=fake.company_email(),
                phone_number=fake.phone_number(),
                loading_country=fake.country(),
                loading_postcode=fake.postcode(),
                loading_city=fake.city(),
                loading_address=fake.street_address(),
                loading_coordinates=fake.latlng(),
                loading_date=fake.iso8601(),
                delivery_country=fake.country(),
                delivery_postcode=fake.postcode(),
                delivery_city=fake.city(),
                delivery_address=fake.street_address(),
                delivery_coordinates=fake.latlng(),
                delivery_date=fake.iso8601(),
                distance=random.randint(500, 1500),
                trailer_type=random.choice(Order.trailer_type.trailer_type),
                cargo_details=random.choice(Cargo.CARGO_TYPES),
                length=random.uniform(8.0, 13.6),
                weight=random.uniform(10.0, 24.0),
                adr=fake.pybool(),
                waste=fake.pybool(),
                currency=random.choice(Order.CURRENCY_CHOICE),
                proposed_price=round(random.uniform(500.00, 5000.00), 2),
                status=random.choice(Order.STATUS_CHOICE),
                remarks=fake.word(),
            )

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
