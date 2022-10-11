from rest_framework.serializers import ModelSerializer

from accounts.models import Customer, Profile
from carrier.models import Vehicle
from shipper.models import Order, Cargo


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ("company", "first_name", "last_name", "email", "is_staff")


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"


class CargoSerializer(ModelSerializer):
    class Meta:
        model = Cargo
        fields = "__all__"
