from django.urls import path
from core.views import start_task, price_task, order_registration

app_name = "core"

urlpatterns = [
    path("start_task/", start_task, name="start_task"),
    path("price_task/", price_task, name="price_task"),
    path("order_registration/", order_registration, name="order_registration"),
]
