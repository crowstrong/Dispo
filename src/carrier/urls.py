from django.urls import path

from carrier.views import CreateVehicleView, MyVehiclesView

app_name = "carrier"

urlpatterns = [
    path("vehicles/", MyVehiclesView.as_view(), name="my_vehicles"),
    path("add_vehicle", CreateVehicleView.as_view(), name="add_vehicle"),
]