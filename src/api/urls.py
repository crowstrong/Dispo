from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from api.views import (CargoCreateView, CargoDeleteView, CargoDetailsView,
                       CargoUpdateView, CargoViewSet, CustomerCreateView,
                       CustomerDeleteView, CustomerDetailsView,
                       CustomerUpdateView, CustomerViewSet, OrderCreateView,
                       OrderDeleteView, OrderDetailsView, OrderUpdateView,
                       OrderViewSet, ProfileCreateView, ProfileDeleteView,
                       ProfileDetailsView, ProfileUpdateView, ProfileViewSet,
                       TrailerCreateView, TrailerDeleteView,
                       TrailerDetailsView, TrailerUpdateView, TrailerViewSet, TruckViewSet, TruckCreateView,
                       TruckDetailsView, TruckUpdateView, TruckDeleteView)

app_name = "api"
routers = routers.DefaultRouter()
routers.register("customers", CustomerViewSet)
routers.register("profiles", ProfileViewSet)
routers.register("orders", OrderViewSet)
routers.register("trucks", TruckViewSet)
routers.register("trailer", TrailerViewSet)
routers.register("cargo", CargoViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Dispo API",
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
    path("truck/<int:pk>/", TruckDetailsView.as_view(), name="api_truck_details"),
    path("truck/create/", TruckCreateView.as_view(), name="api_truck_create"),
    path("truck/update/<int:pk>/", TruckUpdateView.as_view(), name="api_truck_update"),
    path("truck/delete/<int:pk>/", TruckDeleteView.as_view(), name="api_truck_delete"),
    path("trailer/<int:pk>/", TrailerDetailsView.as_view(), name="api_trailer_details"),
    path("trailer/create/", TrailerCreateView.as_view(), name="api_trailer_create"),
    path("trailer/update/<int:pk>/", TrailerUpdateView.as_view(), name="api_trailer_update"),
    path("trailer/delete/<int:pk>/", TrailerDeleteView.as_view(), name="api_trailer_delete"),
    path("cargo/<int:pk>/", CargoDetailsView.as_view(), name="api_cargo_details"),
    path("cargo/create/", CargoCreateView.as_view(), name="api_cargo_create"),
    path("cargo/update/<int:pk>/", CargoUpdateView.as_view(), name="api_cargo_update"),
    path("cargo/delete/<int:pk>/", CargoDeleteView.as_view(), name="api_cargo_delete"),
]
