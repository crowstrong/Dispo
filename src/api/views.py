from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     RetrieveAPIView, UpdateAPIView)
from rest_framework.permissions import (IsAdminUser, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.viewsets import ModelViewSet

from accounts.models import Customer, Profile
from api.serializers import (CargoSerializer, CustomerSerializer,
                             OrderSerializer, ProfileSerializer,
                             TrailerSerializer, TruckSerializer)
from carrier.models import Trailer, Truck
from shipper.models import Cargo, Order


# Customer Views
class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CustomerCreateView(CreateAPIView):
    queryset = Customer
    permission_classes = [IsAdminUser]


class CustomerDetailsView(RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Customer.objects.get(pk=self.kwargs.get("pk"))


class CustomerUpdateView(UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


class CustomerDeleteView(DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]


# Profile Views


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProfileCreateView(CreateAPIView):
    queryset = Profile
    permission_classes = [IsAdminUser]


class ProfileDetailsView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Profile.objects.get(pk=self.kwargs.get("pk"))


class ProfileUpdateView(UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]


class ProfileDeleteView(DestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]


# Order Views


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class OrderCreateView(CreateAPIView):
    queryset = Order
    permission_classes = [IsAuthenticatedOrReadOnly]


class OrderDetailsView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Order.objects.get(pk=self.kwargs.get("pk"))


class OrderUpdateView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class OrderDeleteView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


# Truck Views


class TruckViewSet(ModelViewSet):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer
    permission_classes = [IsAuthenticated]


class TruckCreateView(CreateAPIView):
    queryset = Truck
    permission_classes = [IsAuthenticatedOrReadOnly]


class TruckDetailsView(RetrieveAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Truck.objects.get(pk=self.kwargs.get("pk"))


class TruckUpdateView(UpdateAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer
    permission_classes = [IsAuthenticated]


class TruckDeleteView(DestroyAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer
    permission_classes = [IsAuthenticated]


# Trailer Views


class TrailerViewSet(ModelViewSet):
    queryset = Trailer.objects.all()
    serializer_class = TrailerSerializer
    permission_classes = [IsAdminUser]


class TrailerCreateView(CreateAPIView):
    queryset = Trailer
    permission_classes = [IsAdminUser]


class TrailerDetailsView(RetrieveAPIView):
    queryset = Trailer.objects.all()
    serializer_class = TrailerSerializer
    permission_classes = [IsAdminUser]

    def get_object(self):
        return Trailer.objects.get(pk=self.kwargs.get("pk"))


class TrailerUpdateView(UpdateAPIView):
    queryset = Trailer.objects.all()
    serializer_class = TrailerSerializer
    permission_classes = [IsAdminUser]


class TrailerDeleteView(DestroyAPIView):
    queryset = Trailer.objects.all()
    serializer_class = TrailerSerializer
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
