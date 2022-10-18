from django.contrib.auth import get_user_model
from django.test import TestCase

from carrier.models import Vehicle
from shipper.models import Cargo, Order


class OrderTestCase(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(company="FreightForwarder")
        self.vehicle = Vehicle.objects.create(vehicle="Curtain Trailer")
        self.cargo = Cargo.objects.create(cargo_type="Industry")
        self.order = Order.objects.create(
            user=self.user,
            order_id="f50ec0b7-f960-400d-91f0-c42a6d44e3d0",
            loading_place="Paris",
            loading_date="2022-07-07 00:00:00",
            delivery_place="Berlin",
            delivery_date="2022-07-10 00:00:00",
            distance=1211.5,
            vehicle_type=self.vehicle,
            cargo_details=self.cargo,
            length=13.6,
            weight=22.0,
            adr=False,
            waste=False,
            currency="EUR",
            proposed_price=2400.00,
            status="Actual",
            remarks="Let's do it!!!",
        )
        self.order.save()

    def test_order_model(self):
        self.assertEqual(self.order.user, self.user)
        self.assertEqual(self.order.order_id, "f50ec0b7-f960-400d-91f0-c42a6d44e3d0")
        self.assertEqual(self.order.loading_place, "Paris")
        self.assertEqual(self.order.loading_date, "2022-07-07 00:00:00")
        self.assertEqual(self.order.delivery_place, "Berlin")
        self.assertEqual(self.order.delivery_date, "2022-07-10 00:00:00")
        self.assertEqual(self.order.distance, 1211.5)
        self.assertEqual(self.order.vehicle_type, self.vehicle)
        self.assertEqual(self.order.cargo_details, self.cargo)
        self.assertEqual(self.order.length, 13.6)
        self.assertEqual(self.order.weight, 22.0)
        self.assertEqual(self.order.adr, False)
        self.assertEqual(self.order.waste, False)
        self.assertEqual(self.order.currency, "EUR")
        self.assertEqual(self.order.proposed_price, 2400.00)
        self.assertEqual(self.order.status, "Actual")
        self.assertEqual(self.order.remarks, "Let's do it!!!")

    def test_company_str(self):
        self.assertEqual(str(self.user), "FreightForwarder")

    def test_vehicle_type(self):
        vehicle_types = ["Refrigerator", "Curtain Trailer"]
        for vehicle_type in vehicle_types:
            obj = Vehicle.objects.create(vehicle=vehicle_type)
            self.assertEquals(vehicle_type, obj.vehicle)

    def test_cargo_type(self):
        cargo_types = ["Industry", "Frozen Goods"]
        for cargo_type in cargo_types:
            obj = Cargo.objects.create(cargo_type=cargo_type)
            self.assertEquals(cargo_type, obj.cargo_type)
