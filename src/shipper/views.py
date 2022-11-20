from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from shipper.forms import OrderForm
from shipper.models import Order


class MyOrdersView(ListView):
    model = Order
    template_name = "shipper/my_orders.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = Order.objects.all()
        context["orders"] = orders
        return context


class CreateOrderView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = "shipper/add_order.html"
    success_url = reverse_lazy("shipper:my_orders")


class DetailOrderView(DetailView):
    model = Order
    template_name = "shipper/order_details.html"
    pk_url_kwarg = 'pk'
