from uuid import uuid4

from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

from accounts.managers import CustomerManager, PeopleManager


class Person(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid4,
        unique=True,
        db_index=True,
    )
    company_name = models.CharField(max_length=100, null=True)
    contact_person = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField(max_length=255, blank=False, null=True)
    phone_number = PhoneNumberField(null=True, blank=True)

    def __str__(self):
        return f"{self.contact_person} {self.email}"

    class Meta:
        abstract = True


class Customer(AbstractBaseUser, PermissionsMixin):
    company_name = models.CharField(_("Company name"), max_length=100, null=True)
    contact_person = models.CharField(_("Contact Person"), max_length=100, blank=True, null=True)
    email = models.EmailField(_("Contact Email"), max_length=255, blank=True, null=True, unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. " "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    avatar = models.ImageField(upload_to="media/img/profiles/", blank=True)

    objects = CustomerManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.company_name

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_company_name(self):
        return self.company_name

    def get_working_time(self):
        return f"Time on site: {timezone.now() - self.date_joined}"


class ProxyUser(get_user_model()):
    people = PeopleManager()

    class Meta:
        proxy = True
        ordering = ("-pk",)

    def do_something(self):
        print(f"{self.contact_person}_{self.email}")


class Profile(models.Model):
    SHIPPER = "Shipper"
    CARRIER = "Carrier"
    USER_TYPES = [
        (SHIPPER, "Shipper"),
        (CARRIER, "Carrier"),
    ]
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    user_type = models.CharField(max_length=50, choices=USER_TYPES)
    avatar = models.ImageField(upload_to="img/profiles/", blank=True)
    email = models.EmailField(max_length=100, null=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    location = CountryField(blank_label="(select country)", blank=False)
    web_site = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f"{self.user.company_name} {self.user.contact_person} {self.user.email} {self.user.pk}"

    def get_absolute_url(self):
        return reverse("profile", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
