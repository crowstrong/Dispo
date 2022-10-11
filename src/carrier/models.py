from django.db import models
from django.utils.translation import gettext_lazy as _


class Vehicle(models.Model):
    class VEHICLE_TYPES(models.TextChoices):
        REFRIGERATOR = "Refrigerator", "Refrigerator"
        CURTAIN = "Curtain Trailer", "Curtain Trailer"
        MEGA = "Mega Trailer", "Mega Trailer"
        BOX = "Box Trailer", "Box Trailer"
        CONTAINER = "Container Trailer", "Container Trailer"
        TANKER = "Tanker", "Tanker"

    vehicle = models.CharField(choices=VEHICLE_TYPES.choices, max_length=100, blank=False, null=True)

    def __str__(self):
        return self.vehicle

    class Meta:
        verbose_name = _("Vehicle Type")
        verbose_name_plural = _("Vehicle Types")
