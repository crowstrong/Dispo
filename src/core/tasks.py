import random
import time

from celery import shared_task
from django.contrib.auth import get_user_model
from faker import Faker

from shipper.models import Order
from carrier.models import Truck

fake = Faker()


@shared_task
def task_request():
    time.sleep(random.randint(1, 10))


@shared_task
def get_price(loading_country, loading_postcode, loading_city, delivery_country, delivery_postcode, delivery_city):
    loading_country = fake.country()
    loading_postcode = fake.postcode()
    loading_city = fake.city()
    delivery_country = fake.country()
    delivery_postcode = fake.postcode()
    delivery_city = fake.city()
    print(f"{loading_country}-{loading_postcode} {loading_city} >> {delivery_country}-{delivery_postcode} {delivery_city}")
    distance = random.randint(500, 1500)
    tariff = random.uniform(0.7, 1.2)
    return distance * tariff


@shared_task
def order_request():
    order = Order.objects.create(
        company_name=get_user_model().objects.create_user(),
        contact_person=fake.name(),
        contact_email=fake.company_email(),
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
    )
    order.save()
