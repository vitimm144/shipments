from rest_framework.test import APITestCase
from django.test import TestCase
from core.models import Shipment
from django.urls import reverse
from rest_framework import status
from pprint import pprint


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


class ShipmentTestCase(APITestCase):

    def test_create(self):
        data = {
            "sender_name": "Jose Maria",
            "recipient_name": "Rodrigo Moura",
            "sender_address": "Tereza street, 105, Petrópolis - RJ, Brazil",
            "recipient_address": "Dom Pedro street,  234, Petrópolis - RJ, Brazil",
            "postal_code": "2560000",
            "shipment_code": "3453ffa456"

        }
        url = reverse('shipment-list')
        response = self.client.post(
            url,
            data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_path(self):
        shipment = Shipment.objects.create(
            sender_name="Victor Silva",
            recipient_name="Maria",
            sender_address="Ipiranga street, 78 Petrópolis, RJ Brazil",
            recipient_address="Carmen da Ponte Marcolino street, 166 Petrópolis, RJ Brazil",
            postal_code="25635240",
            shipment_code="223334"

        )

        self.assertTrue(shipment.pk)
        self.assertEqual(shipment.recipient_name, "Maria")

        data = {
            "recipient_name": "Maria Joaquina"
        }
        response = self.client.patch(
            reverse(
                'shipment-detail',
                kwargs={'pk': shipment.pk}
            ),
            data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['recipient_name'], data['recipient_name'])

    def test_edit_put(self):
        shipment = Shipment.objects.create(
            sender_name="Victor Silva",
            recipient_name="Maria",
            sender_address="Ipiranga street, 78 Petrópolis, RJ Brazil",
            recipient_address="Carmen da Ponte Marcolino street, 166 Petrópolis, RJ Brazil",
            postal_code="25635240",
            shipment_code="223334"

        )

        self.assertTrue(shipment.pk)
        self.assertEqual(shipment.recipient_name, "Maria")

        data = {
            "sender_name": "Ricardo Sampaio",
            "recipient_name": "Julio Dias",
            "sender_address": "Santos Dummont street, 55, Petrópolis - RJ, Brazil",
            "recipient_address": "Amazonas street,  678, Petrópolis - RJ, Brazil",
            "postal_code": "25635556",
            "shipment_code": "3453aae5632"

        }

        response = self.client.put(
            reverse(
                'shipment-detail',
                kwargs={'pk': shipment.pk}
            ),
            data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['recipient_name'], data['recipient_name'])
        self.assertEqual(response.data['sender_name'], data['sender_name'])
        self.assertEqual(response.data['sender_address'], data['sender_address'])
        self.assertEqual(response.data['recipient_address'], data['recipient_address'])
        self.assertEqual(response.data['postal_code'], data['postal_code'])
        self.assertEqual(response.data['shipment_code'], data['shipment_code'])

    def test_list(self):
        shipment = Shipment.objects.create(
            sender_name="Samuel Teixeira",
            recipient_name="Vitoria Lima",
            sender_address="Rio de Janeiro street, 78 Petrópolis, RJ Brazil",
            recipient_address="Sgt Boening street, 166 Petrópolis, RJ Brazil",
            postal_code="25635240",
            shipment_code="22567565464"
        )
        self.assertTrue(shipment.pk)
        shipment2 = Shipment.objects.create(
            sender_name="Francisco Silva",
            recipient_name="Rogeria Raposo",
            sender_address="Fazenda Inglesa street, 78 Petrópolis, RJ Brazil",
            recipient_address="São Sebastião street, 166 Petrópolis, RJ Brazil",
            postal_code="25635240",
            shipment_code="223334"

        )
        self.assertTrue(shipment2.pk)
        response = self.client.get(reverse('shipment-list'), {'page_size': 10})
        self.assertEqual(len(response.data['results']), 2)

    def test_delete(self):
        shipment = Shipment.objects.create(
            sender_name="Victor Silva",
            recipient_name="Maria",
            sender_address="Ipiranga street, 78 Petrópolis, RJ Brazil",
            recipient_address="Carmen da Ponte Marcolino street, 166 Petrópolis, RJ Brazil",
            postal_code="25635240",
            shipment_code="223334"

        )
        self.assertTrue(shipment.pk)
        response = self.client.delete(
            reverse(
                'shipment-detail',
                kwargs={'pk': shipment.pk}
            )
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(
            reverse(
                'shipment-detail',
                kwargs={'pk': shipment.pk}
            )
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)