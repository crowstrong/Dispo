import os

from config.settings.base import *  # noqa:

CURRENT_ENV = "PROD"
print(CURRENT_ENV)

DEBUG = False
# SECURITY WARNING: don't run with debug turned on in production!
# TODO update later
ALLOWED_HOSTS = ["localhost", "ec2-44-207-0-126.compute-1.amazonaws.com"]

STATIC_ROOT = os.path.join(BASE_DIR, "static/")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "default_sql": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    },
}
