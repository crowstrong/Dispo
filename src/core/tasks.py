import random
import time

from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from faker import Faker

from config.settings import base

fake = Faker()


@shared_task
def task_request():
    time.sleep(random.randint(1, 10))


@shared_task
def get_price():
    distance = random.randint(500, 1500)
    tariff = random.uniform(0.7, 1.2)
    return distance * tariff


@shared_task
def send_invoices():
    users = get_user_model().objects.all()
    for user in users:
        mail_subject = f"Payment bill for order {fake.uuid4()}"
        message = f"""Please find attached an invoice for {fake.uuid4()} : 
        Loading in {fake.country_code()}-{fake.postcode()} {fake.city()} >> 
        Delivery in {fake.country_code()}-{fake.postcode()} {fake.city()} / Tariff 
        {round(random.uniform(500.00, 5000.00), 2)}"""
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=base.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
        return "Done"
