from carrier.models import Truck
from django.views.generic import CreateView, ListView
from carrier.forms import TruckForm
from django.urls import reverse_lazy


class MyVehiclesView(ListView):
    model = Truck
    template_name = "carrier/my_vehicles.html"


class CreateVehicleView(CreateView):
    model = Truck
    form_class = TruckForm
    template_name = "carrier/add_vehicle.html"
    success_url = reverse_lazy("carrier:my_vehicles")
