from django.http import HttpResponse
from faker import Faker

from mongo_dispo.models import Entry, Order


def create_in_mongo(request):
    faker = Faker()
    orders = [Order(customer=faker.company(), collection=faker.city(), delivery=faker.city(), price=faker.pricetag(),
                    customer_email=faker.company_email(), order_number=faker.pyint()) for _ in range(10)]
    saved = Entry(orders=orders, headline="Requested orders").save()
    return HttpResponse(f"Done: {saved}")


def all_entries(request):
    orders_timestamps = list(Entry.objects.all().values_list("timestamp"))
    return HttpResponse("| ".join([timestamp.strftime("%m-%d-%Y %H:%H:%S") for timestamp in orders_timestamps]))
