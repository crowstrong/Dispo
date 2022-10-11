from django.test import TestCase
# from shipper.models import Order
from carrier.models import Vehicle


class OrderTestCase(TestCase):

    def setUp(self) -> None:
        print("Setting up")

    def test_vehicle_type(self):
        vehicle_types = ["Refrigerator", "Curtain Trailer"]
        for vehicle_type in vehicle_types:
            obj = Vehicle.objects.create(vehicle=vehicle_type)
            self.assertEquals(vehicle_type, obj.vehicle)
