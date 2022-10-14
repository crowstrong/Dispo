from django.urls import path, include
from rest_framework import routers, permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from api.views import (CustomerViewSet, ProfileViewSet, OrderViewSet, VehicleViewSet, CargoViewSet, CustomerDetailsView,
                       CustomerDeleteView, CustomerCreateView, CustomerUpdateView, ProfileDetailsView,
                       ProfileCreateView, ProfileUpdateView, ProfileDeleteView, OrderDetailsView, OrderCreateView,
                       OrderUpdateView, OrderDeleteView, VehicleDetailsView, VehicleCreateView, VehicleUpdateView,
                       VehicleDeleteView, CargoDetailsView, CargoCreateView, CargoUpdateView, CargoDeleteView)

app_name = "api"
routers = routers.DefaultRouter()
routers.register("customers", CustomerViewSet)
routers.register("profiles", ProfileViewSet)
routers.register("orders", OrderViewSet)
routers.register("vehicles", VehicleViewSet)
routers.register("cargo", CargoViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Quizez API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[
        permissions.AllowAny,
    ],
)

urlpatterns = [
    path("", include(routers.urls)),
    path("auth/", include("rest_framework.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger_docs"),
    path("customer/<int:pk>/", CustomerDetailsView.as_view(), name="api_customer_details"),
    path("customer/create/", CustomerCreateView.as_view(), name="api_customer_create"),
    path("customer/update/<int:pk>/", CustomerUpdateView.as_view(), name="api_customer_update"),
    path("customer/delete/<int:pk>/", CustomerDeleteView.as_view(), name="api_customer_delete"),
    path("profile/<int:pk>/", ProfileDetailsView.as_view(), name="api_profile_details"),
    path("profile/create/", ProfileCreateView.as_view(), name="api_profile_create"),
    path("profile/update/<int:pk>/", ProfileUpdateView.as_view(), name="api_profile_update"),
    path("profile/delete/<int:pk>/", ProfileDeleteView.as_view(), name="api_profile_delete"),
    path("order/<int:pk>/", OrderDetailsView.as_view(), name="api_order_details"),
    path("order/create/", OrderCreateView.as_view(), name="api_order_create"),
    path("order/update/<int:pk>/", OrderUpdateView.as_view(), name="api_order_update"),
    path("order/delete/<int:pk>/", OrderDeleteView.as_view(), name="api_order_delete"),
    path("vehicle/<int:pk>/", VehicleDetailsView.as_view(), name="api_vehicle_details"),
    path("vehicle/create/", VehicleCreateView.as_view(), name="api_vehicle_create"),
    path("vehicle/update/<int:pk>/", VehicleUpdateView.as_view(), name="api_vehicle_update"),
    path("vehicle/delete/<int:pk>/", VehicleDeleteView.as_view(), name="api_vehicle_delete"),
    path("cargo/<int:pk>/", CargoDetailsView.as_view(), name="api_cargo_details"),
    path("cargo/create/", CargoCreateView.as_view(), name="api_cargo_create"),
    path("cargo/update/<int:pk>/", CargoUpdateView.as_view(), name="api_cargo_update"),
    path("cargo/delete/<int:pk>/", CargoDeleteView.as_view(), name="api_cargo_delete"),
]
