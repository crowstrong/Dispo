from django.urls import path
from shipper.views import CreateOrderView, MyOrdersView
app_name = "shipper"

urlpatterns = [
    path("orders/", MyOrdersView.as_view(), name="my_orders"),
    path("add_order", CreateOrderView.as_view(), name="add_order"),
]
