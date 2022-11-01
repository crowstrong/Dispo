from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from faker import Faker



class Trailer(models.Model):
    class TRAILER_TYPES(models.TextChoices):
        REFRIGERATOR = "Refrigerator", "Refrigerator"
        CURTAIN = "Curtain Trailer", "Curtain Trailer"
        MEGA = "Mega Trailer", "Mega Trailer"
        BOX = "Box Trailer", "Box Trailer"
        CONTAINER = "Container Trailer", "Container Trailer"
        TANKER = "Tanker", "Tanker"

    trailer = models.CharField(choices=TRAILER_TYPES.choices, max_length=100, blank=False, null=True)

    def __str__(self):
        return self.trailer

    class Meta:
        verbose_name = _("Trailer Type")
        verbose_name_plural = _("Trailer Types")


class Truck(models.Model):
    class TRUCK_STATUS(models.TextChoices):
        ACTUAL = "Actual", "Actual"
        BOOKED = "Booked", "Booked"
        TRANSIT = "Transit", "Transit"
        REJECTED = "Rejected", "Rejected"

    carrier_name = models.CharField(max_length=255, blank=False, null=True)
    vehicle_name = models.CharField(max_length=50, blank=False, null=True)
    truck_registration = CountryField(blank_label="(select country)", blank=False)
    truck_plates = models.CharField(max_length=50, blank=False, null=True)
    trailer_registration = CountryField(blank_label="(select country)", blank=False)
    trailer_plates = models.CharField(max_length=50, blank=False, null=True)
    truck_trailer = models.ForeignKey(
        to="carrier.Trailer", related_name="truck_trailer", on_delete=models.CASCADE, blank=False, null=True)
    truck_status = models.CharField(choices=TRUCK_STATUS.choices, default=TRUCK_STATUS.ACTUAL, blank=False,
                                    max_length=15)

    def __str__(self):
        return f"{self.vehicle_name} {self.truck_plates} {self.trailer_plates}"

    @classmethod
    def generate_instances(cls, count: int) -> None:
        faker = Faker()
        for _ in range(count):
            cls.objects.create(
                carrier_name=faker.company(),
                vehicle_name=faker.bothify(text='??-####', letters='ABCDE'),
                truck_registration=faker.country(),
                truck_plates=faker.license_plate(),
                trailer_registration=faker.country(),
                trailer_plates=faker.license_plate(),
                trailer_type=Trailer.TRAILER_TYPES.CURTAIN,
                truck_status=Truck.TRUCK_STATUS.ACTUAL,
            )

    class Meta:
        verbose_name = _("Trucks")
        verbose_name_plural = _("Trucks")
