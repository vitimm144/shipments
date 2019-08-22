from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from core.models import Shipment


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = (
            "id",
            "sender_name",
            "recipient_name",
            "recipient_address",
            "sender_address",
            "postal_code",
            "shipment_code"
        )
        read_only_fields = (
            "expedition",
        )