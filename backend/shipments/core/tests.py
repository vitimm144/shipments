from django.test import TestCase
from core.models import Shipment
# Create your tests here.


class ShipmentModelTest(TestCase):

    def test_shipment_fields(self):

        shipment = Shipment.objects.create(
            sender_name="Victor Silva",
            recipient_name="Maria",
            sender_address="Ipiranga street, 78 Petrópolis, RJ Brazil",
            recipient_address="Carmen da Ponte Marcolino street, 166 Petrópolis, RJ Brazil",
            postal_code="25635240",
            shipment_code="223334"

        )
        self.assertEqual(shipment.sender_name, "Victor Silva")
        self.assertEqual(shipment.recipient_name, "Maria")
        self.assertEqual(shipment.sender_address, "Ipiranga street, 78 Petrópolis, RJ Brazil")
        self.assertEqual(shipment.recipient_address, "Carmen da Ponte Marcolino street, 166 Petrópolis, RJ Brazil")
        self.assertEqual(shipment.postal_code, "25635240")
        self.assertEqual(shipment.shipment_code, "223334")

