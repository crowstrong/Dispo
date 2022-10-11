from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView

from api.serializers import CustomerSerializer, OrderSerializer, VehicleSerializer, ProfileSerializer, CargoSerializer
from shipper.models import Order, Cargo
from accounts.models import Customer, Profile
from carrier.models import Vehicle


# Customer Views

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerCreateView(CreateAPIView):
    queryset = Customer


class CustomerDetailsView(RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_object(self):
        return Customer.objects.get(pk=self.kwargs.get('pk'))


class CustomerUpdateView(UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDeleteView(DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# Profile Views

class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileCreateView(CreateAPIView):
    queryset = Profile


class ProfileDetailsView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        return Profile.objects.get(pk=self.kwargs.get("pk"))


class ProfileUpdateView(UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDeleteView(DestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# Order Views

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderCreateView(CreateAPIView):
    queryset = Order


class OrderDetailsView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_object(self):
        return Order.objects.get(pk=self.kwargs.get("pk"))


class OrderUpdateView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDeleteView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# Vehicle Views

class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleCreateView(CreateAPIView):
    queryset = Vehicle


class VehicleDetailsView(RetrieveAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def get_object(self):
        return Vehicle.objects.get(pk=self.kwargs.get("pk"))


class VehicleUpdateView(UpdateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleDeleteView(DestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


# Cargo Views

class CargoViewSet(ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer


class CargoCreateView(CreateAPIView):
    queryset = Cargo


class CargoDetailsView(RetrieveAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

    def get_object(self):
        return Cargo.objects.get(pk=self.kwargs.get("pk"))


class CargoUpdateView(UpdateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer


class CargoDeleteView(DestroyAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
