from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from api.serializers import CustomerSerializer, OrderSerializer, VehicleSerializer, ProfileSerializer, CargoSerializer
from shipper.models import Order, Cargo
from accounts.models import Customer, Profile
from carrier.models import Vehicle


# Customer Views

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]



class CustomerCreateView(CreateAPIView):
    queryset = Customer
    permission_classes = [IsAdminUser]


class CustomerDetailsView(RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser | IsAuthenticated]


    def get_object(self):
        return Customer.objects.get(pk=self.kwargs.get('pk'))


class CustomerUpdateView(UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser | IsAuthenticated]


class CustomerDeleteView(DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]


# Profile Views

class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]


class ProfileCreateView(CreateAPIView):
    queryset = Profile
    permission_classes = [IsAdminUser]


class ProfileDetailsView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser | IsAuthenticated]

    def get_object(self):
        return Profile.objects.get(pk=self.kwargs.get("pk"))


class ProfileUpdateView(UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser | IsAuthenticated]


class ProfileDeleteView(DestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]


# Order Views

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser | IsAuthenticated]


class OrderCreateView(CreateAPIView):
    queryset = Order
    permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]


class OrderDetailsView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser | IsAuthenticated]

    def get_object(self):
        return Order.objects.get(pk=self.kwargs.get("pk"))


class OrderUpdateView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser | IsAuthenticated]


class OrderDeleteView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser | IsAuthenticated]


# Vehicle Views

class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAdminUser]


class VehicleCreateView(CreateAPIView):
    queryset = Vehicle
    permission_classes = [IsAdminUser]


class VehicleDetailsView(RetrieveAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAdminUser]

    def get_object(self):
        return Vehicle.objects.get(pk=self.kwargs.get("pk"))


class VehicleUpdateView(UpdateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAdminUser]


class VehicleDeleteView(DestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAdminUser]


# Cargo Views

class CargoViewSet(ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    permission_classes = [IsAdminUser]


class CargoCreateView(CreateAPIView):
    queryset = Cargo
    permission_classes = [IsAdminUser]


class CargoDetailsView(RetrieveAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    permission_classes = [IsAdminUser]

    def get_object(self):
        return Cargo.objects.get(pk=self.kwargs.get("pk"))


class CargoUpdateView(UpdateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    permission_classes = [IsAdminUser]


class CargoDeleteView(DestroyAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    permission_classes = [IsAdminUser]
