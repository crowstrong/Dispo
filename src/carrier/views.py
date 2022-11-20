from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from carrier.forms import TruckForm
from carrier.models import Truck


class MyVehiclesView(ListView):
    model = Truck
    template_name = "carrier/my_vehicles.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trucks = Truck.objects.all()
        context["trucks"] = trucks
        return context


class CreateVehicleView(CreateView):
    model = Truck
    form_class = TruckForm
    template_name = "carrier/add_vehicle.html"
    success_url = reverse_lazy("carrier:my_vehicles")


class DetailTruckView(DetailView):
    model = Truck
    template_name = "carrier/truck_details.html"
    pk_url_kwarg = 'pk'
