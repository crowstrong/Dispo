# Generated by Django 4.1.1 on 2022-10-31 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shipper", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="user",
            new_name="company_name",
        ),
        migrations.RenameField(
            model_name="order",
            old_name="trailer_type",
            new_name="trailer_details",
        ),
    ]
