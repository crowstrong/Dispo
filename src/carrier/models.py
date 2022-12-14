from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from faker import Faker
from accounts.models import Company


class Trailer(models.Model):
    class TRAILER_TYPES(models.TextChoices):
        REFRIGERATOR = "Refrigerator", "Refrigerator"
        CURTAIN = "Curtain Trailer", "Curtain Trailer"
        MEGA = "Mega Trailer", "Mega Trailer"
        BOX = "Box Trailer", "Box Trailer"
        CONTAINER = "Container Trailer", "Container Trailer"
        TANKER = "Tanker", "Tanker"

    trailer = models.CharField(
        choices=TRAILER_TYPES.choices, default=TRAILER_TYPES.CURTAIN, max_length=100, blank=False, null=True
    )

    def __str__(self):
        return self.trailer

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Trailer Type")
        verbose_name_plural = _("Trailer Types")


class Truck(Company):
    class TRUCK_STATUS(models.TextChoices):
        ACTUAL = "Actual", "Actual"
        BOOKED = "Booked", "Booked"
        TRANSIT = "Transit", "Transit"
        REJECTED = "Rejected", "Rejected"

    vehicle_name = models.CharField(max_length=50, blank=False, null=True)
    truck_registration = CountryField(blank_label="(select country)", blank=False)
    truck_plates = models.CharField(max_length=50, blank=False, null=True)
    trailer_registration = CountryField(blank_label="(select country)", blank=False)
    trailer_plates = models.CharField(max_length=50, blank=False, null=True)
    truck_trailer = models.ForeignKey(
        to="carrier.Trailer", related_name="truck_trailer", on_delete=models.CASCADE, blank=False, null=True
    )
    position_country = CountryField(blank_label="(select country)", blank=False)
    position_postcode = models.CharField(max_length=25, blank=False, null=True)
    position_city = models.CharField(max_length=100, blank=False, null=True)
    truck_status = models.CharField(
        choices=TRUCK_STATUS.choices, default=TRUCK_STATUS.ACTUAL, blank=False, max_length=15
    )

    def __str__(self):
        return f"{self.vehicle_name} {self.truck_plates} {self.trailer_plates}"

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
                vehicle_name=fake.bothify(text="??-####", letters="ABCDE"),
                truck_registration=fake.country_code(),
                truck_plates=fake.license_plate(),
                trailer_registration=fake.country_code(),
                trailer_plates=fake.license_plate(),
                truck_trailer=Trailer.objects.create(),
                position_country=fake.country_code(),
                position_postcode=fake.postcode(),
                position_city=fake.city(),
            )

    class Meta:
        verbose_name = _("Truck")
        verbose_name_plural = _("Trucks")
