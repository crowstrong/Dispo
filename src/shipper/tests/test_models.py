import decimal

from django.test import TestCase

from carrier.models import Trailer
from shipper.models import Cargo, Order


class OrderTestCase(TestCase):
    def setUp(self) -> None:
        self.trailer = Trailer.objects.create(trailer="Curtain Trailer")
        self.cargo = Cargo.objects.create(cargo_type="Industry")
        self.order = Order.objects.create(
            order_id="f50ec0b7-f960-400d-91f0-c42a6d44e3d0",
            company_name="FreightForwarder",
            contact_person="John Doe",
            email="johndoe@example.com",
            phone_number="+1235456677",
            loading_country="FR",
            loading_postcode="75000",
            loading_city="Paris",
            loading_address="some place",
            loading_coordinates="48.850258,2.373047",
            loading_date="2006-10-25T14:30+02:00",
            delivery_country="DE",
            delivery_postcode="10997",
            delivery_city="Berlin",
            delivery_address="some place",
            delivery_date="2006-10-25T14:30+02:00",
            distance="1211",
            trailer_type=self.trailer,
            cargo_details=self.cargo,
            length=13.6,
            weight=22.0,
            adr=False,
            waste=False,
            currency="EUR",
            proposed_price=decimal.Decimal(2400),
            status="Actual",
            remarks="Let's do it!!!",
        )
        self.order.save()

    def test_order_model(self):
        self.assertEqual(self.order.order_id, "f50ec0b7-f960-400d-91f0-c42a6d44e3d0")
        self.assertEqual(self.order.company_name, "FreightForwarder")
        self.assertEqual(self.order.contact_person, "John Doe")
        self.assertEqual(self.order.email, "johndoe@example.com")
        self.assertEqual(self.order.phone_number, "+1235456677")
        self.assertEqual(self.order.loading_country, "FR")
        self.assertEqual(self.order.loading_postcode, "75000")
        self.assertEqual(self.order.loading_city, "Paris")
        self.assertEqual(self.order.loading_address, "some place")
        self.assertEqual(self.order.loading_coordinates, "48.850258,2.373047")
        self.assertEqual(self.order.loading_date, "2006-10-25T14:30+02:00")
        self.assertEqual(self.order.delivery_country, "DE")
        self.assertEqual(self.order.delivery_postcode, "10997")
        self.assertEqual(self.order.delivery_city, "Berlin")
        self.assertEqual(self.order.delivery_address, "some place")
        self.assertEqual(self.order.delivery_date, "2006-10-25T14:30+02:00")
        self.assertEqual(self.order.distance, "1211")
        self.assertEqual(self.order.trailer_type, self.trailer)
        self.assertEqual(self.order.cargo_details, self.cargo)
        self.assertEqual(self.order.length, 13.6)
        self.assertEqual(self.order.weight, 22.0)
        self.assertEqual(self.order.adr, False)
        self.assertEqual(self.order.waste, False)
        self.assertEqual(self.order.currency, "EUR")
        self.assertEqual(self.order.proposed_price, decimal.Decimal(2400))
        self.assertEqual(self.order.status, "Actual")
        self.assertEqual(self.order.remarks, "Let's do it!!!")

    def test_trailer_type(self):
        trailers = ["Refrigerator", "Curtain Trailer"]
        for trailer in trailers:
            obj = Trailer.objects.create(trailer=trailer)
            self.assertEquals(trailer, obj.trailer)

    def test_cargo_type(self):
        cargo_types = ["Industry", "Frozen Goods"]
        for cargo_type in cargo_types:
            obj = Cargo.objects.create(cargo_type=cargo_type)
            self.assertEquals(cargo_type, obj.cargo_type)
