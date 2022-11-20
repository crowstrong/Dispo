from django.urls import path

from carrier.views import CreateVehicleView, MyVehiclesView, DetailTruckView

app_name = "carrier"

urlpatterns = [
    path("vehicles/", MyVehiclesView.as_view(), name="my_vehicles"),
    path("add_vehicle", CreateVehicleView.as_view(), name="add_vehicle"),
    path("truck_details/<uuid:pk>", DetailTruckView.as_view(), name="truck_details"),
]
