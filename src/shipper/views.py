from django.views.generic import CreateView, ListView
from shipper.models import Order
from shipper.forms import OrderForm
from django.urls import reverse_lazy


class MyOrdersView(ListView):
    model = Order
    template_name = "shipper/my_orders.html"


class CreateOrderView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = "shipper/add_order.html"
    success_url = reverse_lazy("shipper:my_orders")
