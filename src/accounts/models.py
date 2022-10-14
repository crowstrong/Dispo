from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from accounts.managers import CustomerManager, PeopleManager


class Customer(AbstractBaseUser, PermissionsMixin):
    company = models.CharField(_("company name"), max_length=150, blank=True)
    first_name = models.CharField(_("name"), max_length=150, blank=True)
    last_name = models.CharField(_("surname"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), null=True, unique=True)
    phone_number = PhoneNumberField(_("phone number"), null=True, blank=True)
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
        return self.company

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def get_working_time(self):
        return f"Time on site: {timezone.now() - self.date_joined}"


class ProxyUser(get_user_model()):
    people = PeopleManager()

    class Meta:
        proxy = True
        ordering = ("-pk",)

    def do_something(self):
        print(f"{self.first_name}_{self.email}")


class Profile(models.Model):
    SHIPPER = "Shipper"
    CARRIER = "Carrier"
    USER_TYPES = [
        (SHIPPER, "Shipper"),
        (CARRIER, "Carrier"),
    ]
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    user_type = models.CharField(max_length=50, choices=USER_TYPES)
    avatar = models.ImageField(upload_to="img/profiles/", blank=False)
    birth_date = models.DateField(blank=True, null=True)
    email = models.EmailField(max_length=100, null=True)
    phone_number = PhoneNumberField()
    location = models.CharField(max_length=100, default="")
    web_site = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} {self.user.email} {self.user.pk}"

    def get_absolute_url(self):
        return reverse("profile", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
