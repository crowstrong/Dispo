from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from faker import Faker
import random


class Trailer(models.Model):
    TRAILER_TYPES = (
        ("Refrigerator", "Refrigerator"),
        ("Curtain Trailer", "Curtain Trailer"),
        ("Mega Trailer", "Mega Trailer"),
        ("Box Trailer", "Box Trailer"),
        ("Container Trailer", "Container Trailer"),
        ("Tanker", "Tanker"),
    )

    trailer = models.CharField(choices=TRAILER_TYPES, max_length=100, blank=False, null=True)

    def __str__(self):
        return self.trailer_type

    class Meta:
        verbose_name = _("Trailer Type")
        verbose_name_plural = _("Trailer Types")


class Truck(models.Model):
    TRUCK_STATUS = (
        ("Actual", "Actual"),
        ("Booked", "Booked"),
        ("Transit", "Transit"),
        ("Rejected", "Rejected")
    )

    carrier_name = models.CharField(max_length=255, blank=False, null=True)
    vehicle_name = models.CharField(max_length=50, blank=False, null=True)
    truck_registration = CountryField(blank_label="(select country)", blank=False)
    truck_plates = models.CharField(max_length=50, blank=False, null=True)
    trailer_registration = CountryField(blank_label="(select country)", blank=False)
    trailer_plates = models.CharField(max_length=50, blank=False, null=True)
    truck_trailer = models.ForeignKey(
        to="carrier.Trailer", related_name="truck_trailer", on_delete=models.CASCADE, blank=False, null=True
    )
    truck_status = models.CharField(
        choices=TRUCK_STATUS, default="ACTUAL", blank=False, max_length=15
    )

    def __str__(self):
        return f"{self.vehicle_name} {self.truck_plates} {self.trailer_plates}"

    @classmethod
    def generate_instances(cls, count: int) -> None:
        fake = Faker()
        for _ in range(count):
            cls.objects.create(
                carrier_name=fake.company(),
                vehicle_name=fake.bothify(text="??-####", letters="ABCDE"),
                truck_registration=fake.country(),
                truck_plates=fake.license_plate(),
                trailer_registration=fake.country(),
                trailer_plates=fake.license_plate(),
                truck_trailer=random.choice(
                    ["Refrigerator", "Curtain Trailer", "Mega Trailer", "Box Trailer", "Container Trailer", "Tanker"]),
                truck_status=random.choice(["Actual", "Booked", "Transit", "Rejected"]),
            )

    class Meta:
        verbose_name = _("Trucks")
        verbose_name_plural = _("Trucks")
